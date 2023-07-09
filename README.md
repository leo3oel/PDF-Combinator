# PDF Combinator
Small tool to combine scanned duplex files from two files into one.<br>
The second file also gets reversed.

## Install
There are two ways to use this PDF Combinator:

 1. Download the latest Release (not necessarily up-to-date)
 2. Clone this repo and use python Script (up-to-date)

### Latest Release
There are two types of releases:
 
 1. PDF Combinator with a selection using a gui
 2. PDF Combinator which combines the first two PDFs int the current directory (Tag starting with **noselection_**)

### Python file
Clone this repo, install the required packages using
```
pip install -r packages.txt
```
or the `installPackages.bat` executable.

If required a shortcut can be added to the start menu using `makeShortcut_RUNASADMIN.bat`.

## Usage
Run `pdfCombinator.py` and select the two duplex side, then specify the output location.

Or run `combinePdfsInFolder.py` to combine the first two PDFs in the current working directory