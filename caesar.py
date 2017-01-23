
def alphabet_position(letter):
    return letter


def rotate_char(char,rot):
    return char


def encrypt(message,rot):
    msg=''
    for s in list(message):
        if 0 <= rot <= 13:
            if 'a'<=s<='m': 
                msg+=(chr(ord(s)+rot))
            elif 'n'<=s<='z':
                msg+=(chr(ord(s)-rot))
            elif 'A'<=s<='M':
                msg+=(chr(ord(s)+rot))
            elif  'N'<=s<='Z':
                msg+=(chr(ord(s)-rot))
            else:
                msg+=(s)
        else:
            print('rotate number must be between 0 and 13')
            break        
    return msg


print(encrypt("Message",12))

