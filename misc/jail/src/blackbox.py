from unicodedata import *
gsjg=list('bdefgijklmnopstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./,<>_;:~!@#$%^&*[]{}')
def normalise(string):
    return(normalize('NFKC',string))
def check_blocklist(string):
    for i in string:
        if i in gsjg:
            return(0)
    return(1)