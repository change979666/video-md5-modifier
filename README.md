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

- The original file on disk is never modified. "Modify MD5" writes a `*.tmp` copy,
  appends a few bytes (the current Unix timestamp as ASCII), and you then save that
  copy to a new path of your choice.
- Appending bytes changes the file length and leaves a few trailing bytes outside the
  container. Most tolerant players ignore trailing junk, but some players, upload
  platforms, or strict validators may reject or misplay the file. Compatibility is
  **not guaranteed**; if you need a clean container, re-mux or re-encode the output
  with your own pipeline.
- This tool only changes the on-disk MD5 fingerprint. It is **not** encryption,
  signing, video repair, or a way to bypass content moderation; platforms that
  re-encode or inspect actual streams will still see identical content.

## License & Attribution / 许可与来源

Original project code authored for this repository is released under the MIT License; see [LICENSE](./LICENSE).

When reusing or redistributing a substantial portion, retain the LICENSE and its copyright notice. The copyright notice includes this original source URL: https://github.com/change979666/video-md5-modifier. Please keep the source link visible in your redistributed source or project documentation.

This license applies only to original material that the repository maintainer has the right to license. Third-party libraries, vendor code, platform SDKs, trademarks, screenshots, icons, fonts, and other external assets remain subject to their respective licenses and terms. Review those terms before reuse.

**Project status:** personal/archived project, shared as-is. Maintenance, compatibility, and production readiness are not guaranteed.
