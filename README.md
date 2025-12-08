**subtitle-fix-py**
This Python program corrects the most common character errors in Croatian subtitles.

**About the Program**
This program automatically fixes incorrectly displayed characters in text-based subtitles.
It is useful when characters like č, ć, đ, š, ž are not shown properly (for example, if they appear as "æ", "ð", "ae", etc.).

**What the Program Does**
   Asks the user to enter the name of a .txt subtitle file
   Automatically tries to load the file content using cp1250 encoding, and then utf-8 if the first attempt fails
   Detects and fixes the most common character display errors
   Saves a new, corrected file with the name corrected_[original_name]

**Project Contents**
   ispravak.py – Python script that performs the corrections
   README.md – Instructions for using the program

**How to Use**

1. Check if you have Python installed (version 3.10 or newer).
2. Open ispravak.py in any Python editor
3. Run the program. When the message "Enter the name of the .txt subtitle file (e.g., subtitles.txt)" appears, type the file name (e.g., mymovie.txt).
4. The program will try to open the file using cp1250 encoding. If that fails, it will try utf-8.
5. After successfully loading the file, the program will apply the corrections and save a new file named: corrected_mymovie.txt
6. Open the corrected file and check the result.

**Note on Encoding**
This version of the program attempts to open the file using two of the most common encodings:
   cp1250 (Windows code page for Croatian/East European languages)
   utf-8 (the most widespread text encoding standard)
If neither works, the program will inform the user about the attempted operations.


Author: Iva Široki
