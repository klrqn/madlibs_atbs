#! python3
# Makes a silly madlibs

from pathlib import Path

print('What text file would you like to madlib?')
inFile = Path(input())

# TODO: Read contents of input file for keywords
# ADJECTIVE NOUN VERB

# check path validity
if inFile.is_file():
    inFile.open()
    inText = inFile.read_text()
#    print(inText)
else:
    print('You entered an invalid File')
    return -1

switchWords = ('ADJECTIVE', 'NOUN', 'VERB')


# TODO: Ask User for corresponding words input

# TODO: Write to new text file.

