#returns the number is a palidrone or not (T or F)
def isPal(n):
    hold = str(n)
    test = list(hold)
    test.reverse()
    test = ''.join(test)
    return test == hold

n = 999
num = range(int(n**0.5), n+1)
num.reverse()

#find what is the largest palidrone
largest = 0
for i in num:
    point = i
    while True:
        check = i*point
        if isPal(check):
            if (check) > largest:
                largest = check
            break
        else:
            point-=1

print(largest)
