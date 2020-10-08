str = 'pynative'
num = 9

def removeNChar(str,num):
    if len(str) > num:
        print(str[num:])
    else:
        print("Number is more than the string length : ", num)

removeNChar(str,num)