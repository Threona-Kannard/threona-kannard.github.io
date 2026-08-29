"""
Music Playlist Fetcher (Spotify & YouTube)
==========================================
Crawls all tracks from Spotify or YouTube playlists and exports them to JSON
files compatible with the website.

Supports:
- YouTube Playlists (e.g. https://www.youtube.com/playlist?list=PLbzap-RMQU1Y)
- Spotify Playlists (with direct oEmbed / Web Embed track artwork scraping or official Web API)

Zero external dependencies required (uses standard library).

Usage:
    python scripts/fetch_playlist.py <playlist_url_or_id> <output_name>

Examples:
    python scripts/fetch_playlist.py https://open.spotify.com/playlist/4mYvxCbeZTRUldCJRWzKIi coast-to-coast-playlist
    python scripts/fetch_playlist.py https://www.youtube.com/playlist?list=PLbzap-RMQU1Y childhood-playlist
"""

import argparse
import base64
import html
import http.server
import json
import os
import re
import socketserver
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE = "https://api.spotify.com/v1"

REDIRECT_HOST = "127.0.0.1"
REDIRECT_PORT = 8888
REDIRECT_URI = f"http://{REDIRECT_HOST}:{REDIRECT_PORT}/callback"
SCOPES = "playlist-read-private playlist-read-collaborative"

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent / "src" / "lib" / "data" / "json"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_env_file():
    """Load .env file from project root if it exists."""
    env_path = SCRIPT_DIR.parent / ".env"
    if env_path.exists():
        with open(env_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def detect_platform(url_or_id: str) -> str:
    """Detect whether the input is a YouTube or Spotify URL/ID."""
    if "youtube.com" in url_or_id or "youtu.be" in url_or_id or url_or_id.startswith("PL"):
        return "youtube"
    return "spotify"


def fetch_raw_text(url: str, headers: dict | None = None) -> str:
    """Fetch raw HTML/text from a URL."""
    headers = headers or {}
    headers.setdefault("User-Agent", USER_AGENT)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


def http_request(url: str, method: str = "GET", headers: dict | None = None, data: dict | None = None) -> dict:
    """Execute HTTP request and return parsed JSON."""
    headers = headers or {}
    headers.setdefault("User-Agent", USER_AGENT)
    req_data = None

    if data is not None:
        if headers.get("Content-Type") == "application/json":
            req_data = json.dumps(data).encode("utf-8")
        else:
            req_data = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"HTTP {e.code} Error for {url}: {err_body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error for {url}: {e.reason}") from e


def save_json(data: dict, filepath: Path):
    """Write data to a JSON file with 4-space indentation."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"  [OK] Saved: {filepath}")


# ---------------------------------------------------------------------------
# YouTube Fetcher
# ---------------------------------------------------------------------------

def extract_youtube_playlist_id(url_or_id: str) -> str:
    """Extract playlist ID from a YouTube playlist URL or ID."""
    match = re.search(r"list=([a-zA-Z0-9_-]+)", url_or_id)
    if match:
        return match.group(1)
    if re.fullmatch(r"[a-zA-Z0-9_-]+", url_or_id):
        return url_or_id
    raise ValueError(f"Could not extract YouTube playlist ID from: {url_or_id}")


def extract_text(field: any) -> str:
    """Safely extract plain text from YouTube API/renderer text structures."""
    if not field:
        return ""
    if isinstance(field, str):
        return field
    if isinstance(field, dict):
        if "content" in field:
            return str(field["content"])
        if "simpleText" in field:
            return str(field["simpleText"])
        if "runs" in field and isinstance(field["runs"], list):
            return "".join(r.get("text", "") for r in field["runs"])
    return ""


def parse_youtube_video_entry(item: dict) -> dict | None:
    """Parse a single YouTube video item."""
    if "playlistVideoRenderer" in item:
        v = item["playlistVideoRenderer"]
        video_id = v.get("videoId")
        if not video_id:
            return None
        title = extract_text(v.get("title"))
        artist = extract_text(v.get("shortBylineText"))
        thumbnails = v.get("thumbnail", {}).get("thumbnails", [])
        cover_url = thumbnails[-1]["url"] if thumbnails else f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"

    elif "lockupViewModel" in item:
        v = item["lockupViewModel"]
        video_id = v.get("contentId")
        if not video_id:
            on_tap = v.get("rendererContext", {}).get("commandContext", {}).get("onTap", {})
            watch_ep = on_tap.get("innertubeCommand", {}).get("watchEndpoint", {})
            video_id = watch_ep.get("videoId")
        if not video_id:
            return None

        metadata = v.get("metadata", {}).get("lockupMetadataViewModel", {})
        title = extract_text(metadata.get("title"))

        artist = ""
        metadata_rows = metadata.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", [])
        for row in metadata_rows:
            for part in row.get("metadataParts", []):
                part_text = extract_text(part.get("text"))
                if part_text:
                    artist = part_text
                    break
            if artist:
                break

        if not title:
            accessibility_label = v.get("rendererContext", {}).get("accessibilityContext", {}).get("label", "")
            title = accessibility_label or "Untitled Video"

        cover_url = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        content_img = v.get("contentImage", {}).get("thumbnailViewModel", {}).get("image", {}).get("sources", [])
        if content_img:
            cover_url = content_img[-1].get("url", cover_url)

    else:
        return None

    return {
        "added_at": "",
        "is_local": False,
        "track": {
            "id": video_id,
            "name": title,
            "artists": [
                {
                    "name": artist,
                    "id": "",
                    "href": "",
                    "external_urls": {"spotify": f"https://www.youtube.com/watch?v={video_id}"}
                }
            ],
            "album": {
                "id": "",
                "name": title,
                "images": [{"url": cover_url}],
            },
            "external_urls": {
                "spotify": f"https://www.youtube.com/watch?v={video_id}"
            },
        }
    }


def fetch_youtube_playlist(playlist_id: str) -> tuple[dict, list[dict]]:
    """Fetch YouTube playlist info and all tracks."""
    print(f"Fetching YouTube playlist: {playlist_id}...")
    url = f"https://www.youtube.com/playlist?list={playlist_id}"
    html_content = fetch_raw_text(url)

    match = re.search(r"var ytInitialData = ({.*?});", html_content)
    if not match:
        raise RuntimeError("Could not find YouTube playlist initial data on page.")

    try:
        data = json.loads(match.group(1))
    except Exception as e:
        raise RuntimeError(f"Failed to parse YouTube playlist data: {e}")

    metadata = data.get("metadata", {}).get("playlistMetadataRenderer", {})
    microformat = data.get("microformat", {}).get("microformatDataRenderer", {})

    name = metadata.get("title") or microformat.get("title") or "YouTube Playlist"
    description = metadata.get("description") or microformat.get("description") or ""

    images = []
    og_img = re.search(r'<meta property="og:image" content="(.*?)">', html_content)
    if og_img:
        images.append({"url": og_img.group(1)})
    elif microformat.get("thumbnail", {}).get("thumbnails"):
        images.append({"url": microformat["thumbnail"]["thumbnails"][-1]["url"]})

    playlist_info = {
        "images": images,
        "external_urls": {
            "spotify": f"https://www.youtube.com/playlist?list={playlist_id}"
        },
        "name": name,
        "description": description,
    }

    tracks = []
    try:
        tabs = data.get("contents", {}).get("twoColumnBrowseResultsRenderer", {}).get("tabs", [])
        section_contents = tabs[0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"]
        item_contents = section_contents[0]["itemSectionRenderer"]["contents"]

        if item_contents and "playlistVideoListRenderer" in item_contents[0]:
            raw_items = item_contents[0]["playlistVideoListRenderer"].get("contents", [])
        else:
            raw_items = item_contents

        for item in raw_items:
            track = parse_youtube_video_entry(item)
            if track:
                tracks.append(track)
    except Exception as e:
        print(f"  Warning: Partial error while parsing track list: {e}")

    print(f"  [OK] Successfully fetched {len(tracks)} tracks from YouTube playlist!")
    return playlist_info, tracks


# ---------------------------------------------------------------------------
# Spotify Fetcher
# ---------------------------------------------------------------------------

def extract_spotify_playlist_id(url_or_id: str) -> str:
    """Extract Spotify playlist ID from URL or raw string."""
    match = re.search(r"playlist[/:]([a-zA-Z0-9]+)", url_or_id)
    if match:
        return match.group(1)
    if re.fullmatch(r"[a-zA-Z0-9]{22}", url_or_id):
        return url_or_id
    raise ValueError(f"Could not extract Spotify playlist ID from: {url_or_id}")


def fetch_track_cover_art(track_id: str) -> str | None:
    """
    Fetch accurate, individual album cover art for a track.
    Tries Spotify oEmbed API first (fast and reliable), then falls back to track embed HTML.
    """
    if not track_id:
        return None

    # Method 1: Spotify official public oEmbed API
    try:
        oembed_url = f"https://open.spotify.com/oembed?url=https://open.spotify.com/track/{track_id}"
        data = http_request(oembed_url)
        thumb = data.get("thumbnail_url")
        if thumb:
            return thumb
    except Exception:
        pass

    # Method 2: Track embed HTML page
    try:
        url = f"https://open.spotify.com/embed/track/{track_id}"
        html_content = fetch_raw_text(url)
        og_match = re.search(r'<meta property="og:image" content="(.*?)">', html_content)
        if og_match:
            return og_match.group(1)

        match = re.search(r'<script id="__NEXT_DATA__" type="application/json">({.*?})</script>', html_content)
        if match:
            data = json.loads(match.group(1))
            sources = data.get("props", {}).get("pageProps", {}).get("state", {}).get("data", {}).get("entity", {}).get("coverArt", {}).get("sources", [])
            if sources:
                return sources[0].get("url")
    except Exception:
        pass

    return None


def fetch_via_spotify_embed(playlist_id: str) -> tuple[dict, list[dict]] | None:
    """Scrape playlist info and tracks from the public Spotify embed page."""
    print("Attempting to fetch playlist data from public Spotify page...")
    embed_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"

    try:
        html_content = fetch_raw_text(embed_url)
    except Exception as e:
        print(f"  Warning: Could not fetch embed page ({e}).")
        return None

    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">({.*?})</script>', html_content)
    if not match:
        match = re.search(r'<script id="initial-state" type="text/plain">([A-Za-z0-9+/=]+)</script>', html_content)
        if match:
            try:
                decoded = base64.b64decode(match.group(1)).decode("utf-8")
                raw_json = json.loads(decoded)
            except Exception:
                return None
        else:
            return None
    else:
        try:
            raw_json = json.loads(match.group(1))
        except Exception:
            return None

    entity = None
    try:
        props = raw_json.get("props", {}).get("pageProps", {})
        entity = props.get("state", {}).get("data", {}).get("entity")
    except Exception:
        pass

    if not entity:
        return None

    name = html.unescape(entity.get("name", entity.get("title", "")))
    description = html.unescape(entity.get("subtitle", entity.get("description", "")))
    playlist_images = []
    cover_art = entity.get("coverArt", {}).get("sources", [])
    if cover_art:
        playlist_images.append({"url": cover_art[0].get("url")})
    elif entity.get("images"):
        playlist_images.extend(entity["images"])

    playlist_info = {
        "images": playlist_images,
        "external_urls": {"spotify": f"https://open.spotify.com/playlist/{playlist_id}"},
        "name": name,
        "description": description,
    }

    raw_track_list = entity.get("trackList", [])
    print(f"  Found {len(raw_track_list)} tracks in playlist. Fetching individual album art...")

    # Fetch track covers concurrently
    track_ids = [item.get("id") or item.get("uri", "").split(":")[-1] for item in raw_track_list]
    with ThreadPoolExecutor(max_workers=10) as executor:
        track_covers = list(executor.map(fetch_track_cover_art, track_ids))

    tracks = []
    for idx, item in enumerate(raw_track_list):
        track_id = track_ids[idx]
        track_name = html.unescape(item.get("title", item.get("name", "")))
        artists_str = html.unescape(item.get("subtitle", item.get("artists", "")))
        artists = [{"name": a.strip(), "id": "", "href": "", "external_urls": {"spotify": ""}} for a in artists_str.split(",") if a.strip()]
        duration_ms = item.get("duration", 0)

        album_cover = track_covers[idx]
        album_images = [{"url": album_cover}] if album_cover else playlist_images

        track_obj = {
            "added_at": "",
            "is_local": False,
            "track": {
                "id": track_id,
                "name": track_name,
                "artists": artists,
                "album": {
                    "id": "",
                    "name": track_name,
                    "images": album_images,
                },
                "duration_ms": duration_ms,
                "external_urls": {
                    "spotify": f"https://open.spotify.com/track/{track_id}"
                },
            }
        }
        tracks.append(track_obj)

    print(f"  [OK] Successfully scraped {len(tracks)} tracks with album art!")
    return playlist_info, tracks


class OAuthCallbackHandler(http.server.SimpleHTTPRequestHandler):
    auth_code = None
    error = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if "code" in params:
            OAuthCallbackHandler.auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Authentication successful!</h1><p>You can close this tab and return to the terminal.</p>")
        elif "error" in params:
            OAuthCallbackHandler.error = params["error"][0]
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"<h1>Authentication failed: {OAuthCallbackHandler.error}</h1>".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


def get_spotify_user_token(client_id: str, client_secret: str) -> str:
    """Acquire token using Spotify OAuth2 authorization code flow."""
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
    }
    auth_url = f"{SPOTIFY_AUTH_URL}?{urllib.parse.urlencode(params)}"

    print("Opening browser for Spotify authentication...")
    print(f"If the browser doesn't open automatically, visit:\n  {auth_url}\n")
    webbrowser.open(auth_url)

    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    with ReusableTCPServer((REDIRECT_HOST, REDIRECT_PORT), OAuthCallbackHandler) as httpd:
        httpd.handle_request()

    if OAuthCallbackHandler.error:
        raise RuntimeError(f"Authentication failed: {OAuthCallbackHandler.error}")

    if not OAuthCallbackHandler.auth_code:
        raise RuntimeError("Did not receive authorization code from callback.")

    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("ascii")

    token_data = http_request(
        SPOTIFY_TOKEN_URL,
        method="POST",
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": OAuthCallbackHandler.auth_code,
            "redirect_uri": REDIRECT_URI,
        },
    )
    print("  [OK] Authenticated successfully with Spotify user account!")
    return token_data["access_token"]


def fetch_spotify_api(token: str, playlist_id: str) -> tuple[dict, list[dict]]:
    """Fetch Spotify playlist info and tracks using the official Web API."""
    print("Fetching playlist info via Spotify API...")
    params = urllib.parse.urlencode({"fields": "name,description,images,external_urls"})
    url = f"{SPOTIFY_API_BASE}/playlists/{playlist_id}?{params}"

    playlist_raw = http_request(url, headers={"Authorization": f"Bearer {token}"})
    playlist_info = {
        "images": [{"url": img["url"]} for img in playlist_raw.get("images", [])[:1]],
        "external_urls": playlist_raw.get("external_urls", {}),
        "name": playlist_raw.get("name", ""),
        "description": playlist_raw.get("description", ""),
    }

    tracks = []
    offset = 0
    limit = 100
    print("Fetching tracks via Spotify API...")
    while True:
        params = urllib.parse.urlencode({"limit": limit, "offset": offset})
        track_url = f"{SPOTIFY_API_BASE}/playlists/{playlist_id}/tracks?{params}"
        data = http_request(track_url, headers={"Authorization": f"Bearer {token}"})

        items = data.get("items", [])
        valid_items = [item for item in items if item.get("track") is not None]
        tracks.extend(valid_items)

        total = data.get("total", "?")
        print(f"  Fetched {len(tracks)}/{total} tracks...")

        if not data.get("next"):
            break
        offset += limit

    print(f"  [OK] Total tracks collected: {len(tracks)}")
    return playlist_info, tracks


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Fetch all tracks from a Spotify or YouTube playlist and export to JSON.",
        epilog="Example: python scripts/fetch_playlist.py https://open.spotify.com/playlist/4mYvxCbeZTRUldCJRWzKIi coast-to-coast-playlist",
    )
    parser.add_argument("playlist", help="Spotify or YouTube playlist URL, URI, or ID")
    parser.add_argument("output_name", help="Output file name prefix (e.g. 'coast-to-coast-playlist')")
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help=f"Output directory (default: {OUTPUT_DIR})",
    )
    parser.add_argument(
        "--api", action="store_true",
        help="Force using official Spotify Web API with OAuth login (Spotify only)",
    )
    args = parser.parse_args()

    load_env_file()

    platform = detect_platform(args.playlist)
    print(f"Detected platform: {platform.upper()}")

    playlist_info = None
    tracks = None

    if platform == "youtube":
        try:
            yt_id = extract_youtube_playlist_id(args.playlist)
            print(f"Target YouTube Playlist ID: {yt_id}")
            playlist_info, tracks = fetch_youtube_playlist(yt_id)
        except Exception as e:
            print(f"Error while fetching YouTube playlist: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        # Spotify
        try:
            spotify_id = extract_spotify_playlist_id(args.playlist)
            print(f"Target Spotify Playlist ID: {spotify_id}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

        # 1. Try public web embed scraper first (with oEmbed album art resolution)
        if not args.api:
            result = fetch_via_spotify_embed(spotify_id)
            if result:
                playlist_info, tracks = result

        # 2. Fall back to official Spotify API if needed
        if not tracks:
            print("Using Spotify Web API...")
            client_id = os.environ.get("SPOTIFY_CLIENT_ID")
            client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

            if not client_id or not client_secret:
                print("Error: Spotify API credentials not found in .env file.", file=sys.stderr)
                print("Please add SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET to .env", file=sys.stderr)
                sys.exit(1)

            try:
                token = get_spotify_user_token(client_id, client_secret)
                playlist_info, tracks = fetch_spotify_api(token, spotify_id)
            except Exception as e:
                print(f"Error while fetching from Spotify API: {e}", file=sys.stderr)
                sys.exit(1)

    # Save to disk
    tracks_data = {"tracks": tracks}
    info_data = playlist_info

    output_dir = args.output_dir
    print("Saving files...")
    save_json(tracks_data, output_dir / f"{args.output_name}.json")
    save_json(info_data, output_dir / f"{args.output_name}-info.json")

    print()
    print("Done! [OK]")


if __name__ == "__main__":
    main()
