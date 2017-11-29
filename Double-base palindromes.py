'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

#returns the number is a palidrone or not (T or F)
def isPal(n):
    hold = str(n)
    test = list(hold)
    test.reverse()
    test = ''.join(test)
    return test == hold

def findPals(n):
    num = range(1, n+1)
    
    #find all palidrones
    largest = set()
    for i in num:
        if isPal(i) and isPal(int(bin(i)[2:])) :
            largest.add(i)
    
    return largest

test = findPals(10**6)
