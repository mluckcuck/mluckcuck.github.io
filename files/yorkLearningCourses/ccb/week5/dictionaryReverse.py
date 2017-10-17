""" Reverses a dictionary """

def reverseDict(dictionary):
    """Returns a new dictionary where each item is present in the dictionary
    parameter, but with the key and value swapped"""
    revDict = {}
    for k, v in dictionary.items():
        revDict[v] = k       

    return revDict

