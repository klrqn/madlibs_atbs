#! python3 # Makes a silly madlibs from pathlib import Path

print('What text file would you like to madlib?')
inFile = open(input())
fileString = inFile.read()
inFile.close()

# Split String into list for analysis
wordList = fileString.split()

# Find words to replace in list, replace them with user input
for i in range(len(wordList)):
        if wordList[i] == 'ADJECTIVE':
            print('Give me an Adjective: ')
            a = input()
            wordList[i] = a
        if wordList[i] == 'NOUN':
            print('Give me a Noun: ')
            n = input()
            wordList[i] = n
        if wordList[i] == 'VERB':
            print('Give me a Verb: ')
            v = input()
            wordList[i] = v

# print(f'Word List New = {wordList}')

# Write to new text file.
outFile = open('MaDlIbs.txt', 'w')
madlibs = ' '.join(wordList)
print(f'Madlibs String: {madlibs}')
outFile.write(madlibs)
outFile.close()
