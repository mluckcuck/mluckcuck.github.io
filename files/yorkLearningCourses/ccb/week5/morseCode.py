"""
Translates between plaintext and morse code
"""
morse = {"A":". -", "B":"- . . .", "C":"- . - .", "D":"- . .",
         "E":".", "F":". . - .", "G":"- - .", "H":". . . .", "I":". .",
         "J":". - - -", "K":"- . -", "L":". - . .", "M":"- -", "N":"- .",
         "O":"- - -", "P":". - - .", "Q":"- - . -", "R":". - .", "S":". . .",
         "T":"-", "U":". . -", "V":". . . -", "W":". - -", "X":"- . . -",
         "Y":"- . - -", "Z":"- - . .",
         "1":". - - - -", "2":". . - - -", "3":". . . - -", "4":". . . . -",
         "5":". . . . .", "6":"- . . . .", "7":"- - . . .", "8":"- - - . .",
         "9":"- - - - .", "0":"- - - - -"}



def textToMorse(string):
    pass


def reverseDict(dictionary):
    pass    
    

def morseToText(string):
    pass
    




#Tests

print("SOS Test")
sos = ". . .   - - -   . . ."
result = textToMorse("SOS")
print(result)
print(result == sos)
print()

print("Morse to Text Tests")

string1 =  '. - -   . . . .   . -   -       . . . .   . -   -   . . . .       - - .   - - -   - . .       . - -   . - .   - - -   . . -   - - .   . . . .   -'
string2 = '. . .   . -   - -   . . -   .   . - . .       . . - .   . .   - .   . - . .   .   - . - -       - . . .   . - .   .   .   . . .   .       - -   - - -   . - .   . . .   .'

result1 = morseToText(string1)
print(result1)

result2 = morseToText(string2)
print(result2)

