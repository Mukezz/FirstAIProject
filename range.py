
def sum(num):
    prev = 0
    for i in range(num):
        print("Current Number is ", i, ",Previous number is ", prev, ", Sum is ", i + prev)
        prev = i

sum(10)