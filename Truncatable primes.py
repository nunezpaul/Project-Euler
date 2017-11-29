'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

#Sieve of Eratosthenes
def mark(x, array):
    counter = 1
    while counter < (len(array)-1)/x:
        array[x*(counter+1)] = False
        counter +=1


def findPrime(limit):
    n = limit
    hold = [True]*n
    hold[0], hold[1] = [False]*2 #0 and 1 are not prime numbers
    
    #mark all the multiples as False from 0 to n
    for x in xrange(len(hold)):
        if hold[x]: mark(x,hold)
    
    #initialize sum and index
    primes = set(); index = 1
    while True:
        try:
            index=hold.index(True,index)
            primes.add(index)
            index+=1
        except:
            break
        
    return primes

def remRightPrime(primelist, n):
    hold = str(n)
    if len(hold) > 1:
        hold = int(hold[:-1])
        if hold in primelist:
            return remRightPrime(primelist, hold)
        else:
            return False
    elif int(hold) in primelist:
        return True
    else:
        return False
    
def remLeftPrime(primelist, n):
    hold = str(n)
    if len(hold) > 1:
        hold = int(hold[1:])
        if hold in primelist:
            return remLeftPrime(primelist, hold)
        else:
            return False
    elif int(hold) in primelist:
        return True
    else:
        return False
    
def testing(primelist, n):
    if remLeftPrime(primelist, n) and remRightPrime(primelist,n):
        return n    
        
from functools import partial

def answer(max_num = 10**6):
    n = list(findPrime(max_num)); n.sort(); n = n[4:]
    primelist = findPrime(max_num)
    
    
    test = map(partial(testing, findPrime(max_num)),n)
    
    sum = 0
    for i in test:
        if not(i is None):
            sum += i
    return sum

result = answer()
