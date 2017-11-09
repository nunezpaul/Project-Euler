#Sieve of Eratosthenes

#Mark where there is a multiple as False
def mark(x, array):
    counter = 1
    while counter < (len(array)-1)/x:
        array[x*(counter+1)] = False
        counter +=1



def sumPrime(limit):
    n = limit
    hold = [True]*n
    hold[0], hold[1] = [False]*2 #0 and 1 are not prime numbers
    
    #mark all the multiples as False from 0 to n
    for x in xrange(len(hold)):
        if hold[x]: mark(x,hold)
    
    #initialize sum and index
    sum = 0; index = 0
    while True:
        try:
            index=hold.index(True,index)
            sum+=index
            index+=1
        except:
            break
        
    print("answer is: %d" % (sum) )
    
sumPrime(10)
