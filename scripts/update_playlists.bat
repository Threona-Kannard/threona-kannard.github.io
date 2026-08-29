@echo off
setlocal enabledelayedexpansion

echo ===================================================
echo       UPDATING ALL PLAYLISTS DATA
echo ===================================================
echo.

cd /d "%~dp0\.."

echo [1/5] Updating: Childhood (YouTube)...
python scripts\fetch_playlist.py "https://www.youtube.com/playlist?list=PLbzap-RMQU1Y" childhood-playlist
echo.

echo [2/5] Updating: Coast to Coast (Spotify)...
python scripts\fetch_playlist.py "https://open.spotify.com/playlist/4mYvxCbeZTRUldCJRWzKIi" coast-to-coast-playlist
echo.

echo [3/5] Updating: Hero's Journey (Spotify)...
python scripts\fetch_playlist.py "https://open.spotify.com/playlist/07dhhOD7LYckmIlGQIdDOU" hero-journey-playlist
echo.

echo [4/5] Updating: Moonlight / Tsukikage (Spotify)...
python scripts\fetch_playlist.py "https://open.spotify.com/playlist/33PIrYnFcJXko0sTmRm8RK" moonlight-playlist
echo.

echo [5/5] Updating: Radio Gac Xep (Spotify)...
python scripts\fetch_playlist.py "https://open.spotify.com/playlist/0Y3fqWq3cB2XPCrJEsM7BA" radio-gac-xep-playlist
echo.

echo ===================================================
echo       ALL PLAYLISTS UPDATED SUCCESSFULLY!
echo ===================================================
echo.
pause

