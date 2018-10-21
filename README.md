# These are some desktop applications.

They are written to compare textfiles and to identify duplicate string patterns.

# MissingFiles.py
This program may run out of memory for very large text files. This shortcoming is due to the fact that dictionaries are read entirely and stored in memory. Consider using generator comprehension rather than list/dictionary comprehension to conserve memory. Then use next() method to go through the generator. But at some point you may need to break the file into smaller pieces. To do that, you can write smaller chunks of the textfile in to separate textfiles using a loop structure and then run the program on each smaller piece.
