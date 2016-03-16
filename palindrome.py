import re


def subbing(arg):
    return re.sub(r'\W+', "", arg)


def palindrome(string):
    string = string.lower()
    string = subbing(string)
    if len(string) == 0 or len(string) == 1:
        return True
    elif string[0] != string[len(string)-1]:
        return False
    else:
        return palindrome(string[1:len(string)-1])
