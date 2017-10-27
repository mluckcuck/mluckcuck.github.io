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

def loadStringFrom(fileName):
	try:
		inputFile = open(fileName)
	except FileNotFoundError:
		print("Oops")
		return ""
		
	else:
		string = inputFile.read() #Only works if the file is only one line
		inputFile.close()
		return string

def saveLettersTo(fileName):
	try:
		dataFile = open(fileName, "w")
	except FileNotFoundError:
		print("Oops")
		
	else:
		print(letters)
		for k,v in letters.items():
			dataFile.write(k + "=" + str(v) +"\n")
		dataFile.close()


string = loadStringFrom("inputString.txt")	
print(string)
	
letters = count(string)

saveLettersTo("outputFile.txt")

	
		
