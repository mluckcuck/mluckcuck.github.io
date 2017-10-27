""" Finds the longest in a list of words """

def loadWordList(fileName):
        try:
                f = open(fileName)
        except FileNotFoundError as err:
                print(err)
                
                #Then do something useful
                #Perhaps ask the user for the file name?
                return []
        else:
                loadedList = f.read().splitlines()
                f.close()
                return loadedList

def longestWordLength(wordList):
	""" Returns the length of the longest word"""
	longestLen = 0

	for word in wordList:
		wordLen = len(word)
		if wordLen > longestLen:
			longestLen = wordLen


	return longestLen


def longestWord(wordList):
	"""Returns the longest word"""
	longestWord = ""

	for word in wordList:
		wordLen = len(word)
		if wordLen > len(longestWord):
			longestWord = word


	return longestWord

fileName = "wordListFile.txt"

wordList = loadWordList(fileName)

print(longestWordLength(wordList))

longest = longestWord(wordList)
print("The longest word in the list is", longest, "and it is", len(longest), "characters long" )
