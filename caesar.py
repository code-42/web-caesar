# Functions to be used by all classes
def alphabet_position(letter):
    """Returns the relative position of a particular character
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pos = 0
    for ltr in alphabet:
        if ltr == letter.lower():
            return pos
        pos += 1
    return pos

def rotate_character(char, rot):
    """Returns the character that is the result of moving char by rot
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.lower() not in alphabet:
        return char
    mod = (alphabet_position(char) + rot) % 26
    if char in alphabet:
        newChar = chr(97 + mod)
    else:
        newChar = chr(65 + mod)
    return newChar

def encrypt(text, rot):
    """Takes a string and rotates each character by a given amount, returns a new string
    """
    newText = ""
    for ltr in text:
        newChar = rotate_character(ltr, rot)
        newText += newChar
    return newText
