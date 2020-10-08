str = 'pynative'

def printeven(str):
    length = len(str)
    i = 0
    while i < length:
        if i % 2 == 0: 
            print(str[i])
        i = i + 1

printeven(str)