# Scripts

Hello! These are some helper scripts I use to manage content on the site. 🛠️

---

## 📸 `add_gallery_entry.py`

Adds a new gallery entry to the translation file by scanning a folder of images/videos.

### Usage

```bash
python scripts/add_gallery_entry.py \
  --file src/translations/en.json \
  --folder src/lib/assets/images/galleries/<gallery_folder> \
  --title "Gallery Title" \
  --date "MM YYYY" \
  --variant featured
```

### Arguments

| Argument    | Required | Default       | Description                                                        |
| ----------- | -------- | ------------- | ------------------------------------------------------------------ |
| `--file`    | ✅       | —             | Path to the translation JSON file (e.g.`src/translations/en.json`) |
| `--folder`  | ✅       | —             | Path to the folder containing gallery images/videos                |
| `--title`   |          | `New gallery` | Display title of the gallery                                       |
| `--date`    |          | `01 2025`     | Date string shown on the gallery (format:`MM YYYY`)                |
| `--variant` |          | `featured`    | Gallery variant/layout type                                        |

### Example

```bash
python scripts/add_gallery_entry.py \
  --file src/translations/en.json \
  --folder src/lib/assets/images/galleries/buildnbrew25 \
  --title "Saigon Build&Brew" \
  --date "05 2025" \
  --variant featured
```

### Notes

- Supported file types: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.mp4`, `.webm`, `.mov`, `.avi`, `.ogg`
- Files are sorted numerically (by the last number found in the filename)
- If a gallery with the same title already exists, it will be **updated** instead of duplicated
- Scans subdirectories recursively
- No external dependencies — uses only Python standard library

---

## 🎵 `fetch_playlist.py`

Fetches all tracks from a **YouTube** or **Spotify** playlist and exports them to JSON files that the site can consume.

### Usage

```bash
python scripts/fetch_playlist.py <playlist_url_or_id> <output_name>
```

### Examples

**YouTube Playlist:**

```bash
python scripts/fetch_playlist.py https://www.youtube.com/playlist?list=PLbzap-RMQU1Y childhood-playlist
```

**Spotify Playlist:**

```bash
python scripts/fetch_playlist.py https://open.spotify.com/playlist/1Sg1KUpvncU7SmcRcFILhW sao-playlist
```

### Arguments

| Argument              | Required | Description                                             |
| --------------------- | -------- | ------------------------------------------------------- |
| `playlist`            | ✅       | YouTube or Spotify playlist URL, URI, or ID             |
| `output_name`         | ✅       | Output file name prefix                                 |
| `-o` / `--output-dir` |          | Custom output directory (default: `src/lib/data/json/`) |
| `--api`               |          | Force official Spotify Web API (Spotify only)           |

### Output Files

This generates two files in `src/lib/data/json/`:

| File                      | Content                                            |
| ------------------------- | -------------------------------------------------- |
| `<output_name>.json`      | `{ "tracks": [...] }` — all tracks in the playlist |
| `<output_name>-info.json` | `{ images, external_urls, name, description }`     |

### Accepted playlist formats

**YouTube:**

```
https://www.youtube.com/playlist?list=PLbzap-RMQU1Y
PLbzap-RMQU1Y
```

**Spotify:**

```
https://open.spotify.com/playlist/1Sg1KUpvncU7SmcRcFILhW
https://open.spotify.com/playlist/1Sg1KUpvncU7SmcRcFILhW?si=abc123
spotify:playlist:1Sg1KUpvncU7SmcRcFILhW
1Sg1KUpvncU7SmcRcFILhW
```

### Notes

- Zero setup/authentication required for YouTube playlists and public Spotify playlists!
- Outputs matching schema with cover image, video/song title, artist/channel name, and link.
- Handles pagination automatically — works with playlists of any size
- Skips deleted/unavailable tracks
- Output format matches the existing JSON files used by the site

---

## ⚡ `update_playlists.bat`

A 1-click Windows batch script that automatically updates all 5 playlists configured on your music page:

1. **Childhood** _(YouTube)_
2. **Coast to Coast** _(Spotify)_
3. **Hero's Journey** _(Spotify)_
4. **月光 (Moonlight)** _(Spotify)_
5. **Radio Gác Xép** _(Spotify)_

### Usage

Double-click `scripts/update_playlists.bat` in Windows Explorer or run from terminal:

```cmd
scripts\update_playlists.bat
```
