""" Finds the longest in a list of words """

wordList = ["Dog", "Pig", "Cat", "Horse" ,"Octopus"]

def longestWordLength(wordList):
    """ Returns the length of the longest word"""
    longestLen = 0

    for word in wordList:
        wordLen = len(word)
        if wordLen > longestLen:
            longestLen = wordLen


    return longestLen


print(longestWordLength(wordList))


def longestWord(wordList):
    """Returns the longest word"""
    longestWord = ""

    for word in wordList:
        wordLen = len(word)
        if wordLen > len(longestWord):
            longestWord = word


    return longestWord

longest = longestWord(wordList)
print("The longest word in the list is", longest, " and it is", len(longest), "characters long" )
