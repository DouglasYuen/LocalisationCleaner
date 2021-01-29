# LocalisationCleaner

This simple Python script is intended for use with the **Localizable.strings** in iOS app projects, which is where translation data is added as key-value pairs. On more complex projects with many strings multiple languages, it can be a cumbersome process to add a new language, since this would entail going through every line in the **Localizable.strings** file and removing the value, before passing the file to a translator.

**LocalisationCleaner** addresses this, allowing the user to easily clean up a localisation file with a single Python script, keeping all of the keys and leaving the file ready to accept the translated strings!


## Usage

To use **LocalisationCleaner**, type the following into the Terminal:

    python3 LocalisationCleaner.py <input name> <output name>

Note that the .strings extension is not required.

## Expected Output

*Original input line*

"KEY_STRING" = "Value in English";

*Output line*

"KEY_STRING" = "";

## Compatibility

 - Python 3.9.1, works on Windows 7 and newer, Mac OS X and newer
