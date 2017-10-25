""" Build a dictionary (letters) that maps each letter found in the string
to the number of times it occurs in the string
"""
letters = dict()

string = "the quick brown, fox jumps over the lazy dog"


def count(string):
	letters = dict()
	
	for char in string:
		if char.isalpha():
			if char in letters.keys():
				currentNum = letters[char]
				letters[char] = currentNum +1
			else:
				letters[char] = 1

	return letters

letters = count(string)
print(letters)


