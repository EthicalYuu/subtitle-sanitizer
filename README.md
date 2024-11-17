# Subtitle Sanitizer

## Description
This Python script utilizes Tkinter to create a simple GUI for purifying subtitles by replacing certain words with their alternatives. The word replacements are read from a file named `word_alt.txt`.

### Example
For instance, if the word `damn` is found in the subtitles, and the `word_alt.txt` file specifies `darn` as its alternative, the script will replace all instances of `damn` with `darn` to create a cleaner version of the subtitles.


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

## Future Improvements
While this script serves its purpose of purifying subtitles, there are several areas where it could be enhanced:

1. **Code Refactoring**  
   - The current code was written when I first started programming. It could benefit from refactoring to improve readability, efficiency, and maintainability. 

2. **Dynamic Word Replacement List**  
   - Add functionality to allow users to dynamically update the word replacement list through the GUI without editing the `word_alt.txt` file manually.

3. **Customization Options**  
   - Allow users to choose between different levels of filtering, such as mild, moderate, or strict replacement.

4. **Error Handling**  
   - Implement robust error handling to manage issues like missing files or invalid formats gracefully.

5. **Enhanced GUI Design**  
   - Improve the interface to make it more intuitive, visually appealing, and user-friendly.

6. **Preview and Confirm Changes**  
   - Add a feature to preview changes and confirm or reject individual replacements before saving the purified subtitles.

