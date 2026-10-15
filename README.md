# video-md5-modifier

A tiny Tkinter desktop utility that recomputes the MD5 checksum of a video file and,
on demand, produces a new copy with a deliberately different MD5 by appending a
timestamp to the file bytes. Useful when tools that fingerprint uploads by file hash
treat identical-content videos as duplicates.

## Features

- Pick a video (`mp4 / avi / mov / mkv`) and instantly see its original MD5.
- "Modify MD5" copies the file to a temp file, appends the current Unix timestamp as
  raw bytes, and shows the new MD5.
- Save the modified copy to a path you choose; the temp file is moved into place.
- MD5 is computed in streaming 8 KB chunks, so large videos do not load fully into
  memory.

## Project layout

- `video_md5_modifier.py` — single-file Tkinter app (`MD5ModifierApp`).

## Run

```bash
python video_md5_modifier.py
```

No third-party dependencies — only the Python standard library (`tkinter`, `hashlib`,
`os`, `shutil`, `datetime`).

## Notes

- Appending bytes changes the file length; the modified copy is meant to be re-muxed
  or re-encoded by your own pipeline if you need a clean container.