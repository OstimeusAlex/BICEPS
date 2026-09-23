# "Basic" Input Config for ExoPlaSim (BICEPS)
![BICEPS Icon](data/images/BICEPS.png "BICEPS Icon")
A "basic" input config GUI for the purposes of creating an [ExoPlaSim](https://github.com/alphaparrot/ExoPlaSim) input file. This is the successor of [EPS-IC](https://github.com/OstimeusAlex/ExoPlaSim-InCon/).

## Preview
<img src="https://github.com/OstimeusAlex/BICEPS/data/images/Preview.png" width="48">

## Features
- [x] Easy-to-use layout, sorted into categorised tabs.
- [x] Image->SRA file converter for easy geographic implementation.
- [x] Import/Export Preset Files, saving the hassle of redoing settings.
- [x] Helpful tips via clicking on coloured-text.
- [x] Use of PYSimpleGUI themes (>150 Themes to choose from!).
- [x] Works on multiple platforms (Has been tested on Linux and should work on Windows, needs testing on Mac).
  - _NOTE: ExoPlaSim as of now still operates in a Linux-based environment, this just makes it easier for those less skilled in programming._
## Future Ideas
- [ ] Complete compatibility checker, to warn the user if something will mess up or crash ExoPlaSim.
- [ ] Import directly from ExoPlaSim .py file, this may or may not be possible.

Any other ideas/suggestions welcome!

### Compatibility
- Linux: **Yes** (Tested on Mint/Ubuntu)
- Windows: Not been tested yet, but should work.
- Mac: Not been tested yet.

## Requirements
- PYSimpleGUI
- PIL
- numpy
- shutil
- pathlib

## Instillation
- If you're using windows, then just download the source code, make sure you have the required python modules installed, and then use the BICEPS.py file to get started. There's **no need** to transfer this into WSL.
- If on Linux, do the same as windows, but open it using `python3 BICEPS.py`.
