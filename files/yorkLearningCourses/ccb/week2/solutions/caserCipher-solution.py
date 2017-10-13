""" Provides methods to encrypt and decrypt strings using the Caser cipher.

    Note: this version does not solve the Challenge section
"""

def encrypt(string, offset):
    output = ""
    string = string.lower()

    for char in string:
        if char.isalpha():
            newCharNum = ord(char) + offset
            if newCharNum > 122:
                newCharNum = 96 + (newCharNum - 122)

            output += chr(newCharNum)
        else:
            output += char
    return output

def decrypt(string, offset):
    output = ""
    string = string.lower()

    for char in string:
        if char.isalpha():
            newCharNum = ord(char) - offset
            if newCharNum < 97:
                newCharNum = 122 - (96 - newCharNum)
            output += chr(newCharNum)
        else:
            output += char
            
    return output

#######Tests###########

print(encrypt("a",1)) #b

print(encrypt("b", 2)) #d

print(encrypt("z", 1)) #a

print(encrypt("A", 3)) #d

print(encrypt("Z", 1)) #a

print(encrypt("This Is A Test",5)) # ymnx nx f yjxy

print(decrypt("a",1)) #z

print(decrypt("b", 2)) #z

print(decrypt("z", 1)) #y

print(decrypt("A", 3)) #x

print(decrypt("Z", 1)) #y

print(decrypt(encrypt("This Is A Test",5),5)) # this is a test

