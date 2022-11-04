# PNG Sanitizer

# Description
Santize PNGs in a folder for use in applications utilizing FFMPEG

# Requirements
- FFMPEG

# Usage
Supply a directory with pngs as ```inputDirectory``` to scan a directory. If no directory is provided, the current launch directory will be scanned.
```python
pyton main.py -i {inputDirectory}
```

# Build
Run the buildExe.bat file in a python environment with ```pyinstaller``` properly installed.