morse = {"A":". -", "B":"- . . .", "C":"- . - .", "D":"- . .",
         "E":".", "F":". . - .", "G":"- - .", "H":". . . .", "I":". .",
         "J":". - - -", "K":"- . -", "L":". - . .", "M":"- -", "N":"- .",
         "O":"- - -", "P":". - - .", "Q":"- - . -", "R":". - .", "S":". . .",
         "T":"-", "U":". . -", "V":". . . -", "W":". - -", "X":"- . . -",
         "Y":"- . - -", "Z":"- - . .",
         "1":". - - - -", "2":". . - - -", "3":". . . - -", "4":". . . . -",
         "5":". . . . .", "6":"- . . . .", "7":"- - . . .", "8":"- - - . .",
         "9":"- - - - .", "0":"- - - - -"}

def reverseDict(dictionary):
    
    revDict = {}
    for k, v in dictionary.items():
        revDict[v] = k       

    return revDict

def textToMorse(string):
    string = string.upper()
    output = ""

    words = string.split(" ")
    for i in range(len(words)):
        word = words[i]

        for j in range(len(word)) :
            if word[j] in morse.keys():
                output += morse[word[j]]

                if j < len(word)-1:
                    output +="   "
        if i < len(words) -1:
            output += "       "

    return output


def morseToText(string):
  
    output = ""

    reversedMorse = reverseDict(morse)

    words = string.split("       ")
    for i in range(len(words)):
        word = words[i]

        letters = word.split("   ")

        for j in range(len(letters)) :
            if letters[j] in reversedMorse.keys():
                output += reversedMorse[letters[j]] #

                
        if i < len(words) -1:
            output += " "

    return output

    




#Tests

print("SOS Test")
sos = ". . .   - - -   . . ."
result = textToMorse("SOS")
print(result)
print(result == sos)
print()

print("Help Me Test")
helpMe = ". . . .   .   . - . .   . - - .       - -   ."
result = textToMorse("Help Me")
print(result)
print(result == helpMe)
print()

print("Morse to Text Tests")
print()

print("SOS Reverse Test")
sos = ". . .   - - -   . . ."
result = morseToText(sos)
print(result)
print(result == "SOS")
print()

print("Help Me Reverse Test")
helpMe = ". . . .   .   . - . .   . - - .       - -   ."
result = morseToText(helpMe)
print(result)
print(result == "HELP ME")



string1 =  '. - -   . . . .   . -   -       . . . .   . -   -   . . . .       - - .   - - -   - . .       . - -   . - .   - - -   . . -   - - .   . . . .   -'
string2 = '. . .   . -   - -   . . -   .   . - . .       . . - .   . .   - .   . - . .   .   - . - -       - . . .   . - .   .   .   . . .   .       - -   - - -   . - .   . . .   .'

result1 = morseToText(string1)
print(result1)

result2 = morseToText(string2)
print(result2)
