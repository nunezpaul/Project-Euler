'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def factorial(n):
    product = 1
    for i in range(1,int(n)+1):
        product = product*i
    return product

def search():
    keep = []
    for i in range(3,10**7):
        test = str(i)
        test = list(test)
        test = map(factorial, test)
        if i == sum(test):
            keep.append(i)
            print(i)
    return keep

answer = sum(search())
