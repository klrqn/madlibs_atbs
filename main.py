#! python3
# Makes a silly madlibs

from pathlib import Path

print('What text file would you like to madlib?')
inFile = open(input())

# TODO: Read contents of input file for keywords
# ADJECTIVE NOUN VERB

# check path validity
#if inFile.is_file():
#    inFile.open()
#    inText = inFile.read_text()
#    inFile.close()
#    print(inText)
#else:
#    print('You entered an invalid File')

switchWords = ('ADJECTIVE', 'NOUN', 'VERB')

fileString = inFile.read()
wordList = fileString.split()
print(wordList)


# TODO: Ask User for corresponding words input



# TODO: Write to new text file.

