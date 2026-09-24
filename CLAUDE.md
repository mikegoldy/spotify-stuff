# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal collection of Python scripts, Jupyter notebooks, and one R script built on the Spotify Web API (via `spotipy`). It does three things: migrates an Apple Music library to Spotify, pulls per-track audio features into CSVs, and runs statistical analysis on those CSVs. There is no package, build system, dependency manifest, linter, or test suite. `test.py` is a scratch script that prints current playback; it is not a test.

## Running things

- Scripts run top to bottom: each calls `main()` at module level, so importing one executes it.
  - `python createSpotifyLibraryFromCsv.py`: prompts for a playlist name, opens a Tk file picker for the Apple Music CSV, creates the playlist, and writes unmatched songs to `missingSongs2.csv`.
  - `python getPlaylistData.py`: the input playlist ID (`playlist_id`) and output filename (`fillCsv` → `playlistEthanTrip.csv`) are hardcoded; edit them before each run.
- Notebooks: `jupyter notebook <name>.ipynb`. They read CSVs from absolute paths on the author's Mac (`/Users/michaelgoldfeld/Documents/Python projects/Spotify/...`). Change those to repo-relative paths to run them anywhere else. `MusicAnalysis.R` has the same problem with a `~/Documents/...` path.
- Dependencies (inferred from imports, not pinned anywhere): `spotipy`, `pandas`, `matplotlib`, `seaborn`, `numpy`, `tkinter`.

## Authentication: `SpotifyCred` is missing

Every script and `playlistCreation.ipynb` does `import SpotifyCred` and calls `SpotifyCred.spotifyCreds()` to get an authenticated `spotipy.Spotify` client. That module is **not in the repo** (the README lists encrypting the login as future work). To run anything, first create `SpotifyCred.py` with a `spotifyCreds()` function that returns a `spotipy.Spotify` client authorized with playlist read/modify scopes, e.g. using `spotipy.oauth2.SpotifyOAuth`. Keep it out of git. spotipy caches tokens in `.cache-<username>` files. `.gitignore` covers only `.cache-12120259561`, so `.cache-luis_ferxis` is committed.

## Data flow

1. **Apple Music export → Spotify playlist** (`createSpotifyLibraryFromCsv.py`): the input CSV comes from copying the Apple Music library into a spreadsheet, so it has no header (see `appleMusicLibrary.csv`). `readCsv` assigns positional column names and keeps only column 0 (song) and column 3 (artist). When a search misses, `missingTrack` and `missingArtist` strip "feat.", "&", "(Original Mix)" and similar, then retry once. `GUIDE TO USING createSpotifyLibrary.pdf` gives the end-user steps.
2. **Playlist → feature CSV** (`getPlaylistData.py`): pages through the playlist 100 tracks at a time and calls `sp.audio_features` per track. It writes a CSV with an unnamed index column followed by `name, artist, duration, key, mode, beats, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, valence, tempo, popularity, URI`. The committed `playlist*.csv` files use this schema: `playlistInfo.csv` is the author's library, `playlistBo.csv` is a friend's, `playlistInfoPopular.csv` is the US Top 50.
3. **Analysis**: the notebooks and `MusicAnalysis.R` load those CSVs, index by `name`, and drop the leading index column. `playlistCreation.ipynb` filters tracks on feature thresholds (e.g. energy > .75) and writes them back to new Spotify playlists.

Spotify restricted the audio-features endpoint for newly registered apps in late 2024. `getPlaylistData.py` may fail on a new app's credentials, and it silently skips tracks when `audio_features` raises an exception.
