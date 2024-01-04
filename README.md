# Sub Purifier

## Description

This Python script utilizes Tkinter to create a simple GUI for purifying subtitles by replacing certain words with their alternatives. The word replacements are read from a file named "word_alt.txt."

## Features

- Browse and select subtitle files (ASS format).
- View selected subtitle files in a list.
- Purify selected subtitle files by replacing words with their alternatives.
- Reset the list of selected subtitle files.

## Usage

1. **Run the script by executing the Python file:**

   ```
   python sub_purifier.py
   ```

## Dependencies
- _Tkinter_ : GUI library for Python.
- _pysubs2_ : Subtitle manipulation library.<br>

## Install dependencies using:

```
pip install tk
pip install pysubs2
```

## File Structure
- _sub_purifier.py_ : Main script for the Sub Purifier.
- _purifier.py_ : Module containing functions for word replacement in subtitles.
- _word_alt.txt_ : File containing word replacements.
