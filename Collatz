#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

def powerof2(x):
    return (x & (x - 1)) == 0

def Collatz(max_n):
    cache = {}
    for n in xrange(2,max_n+1):
        start = n
        count = 1
        while True:
            if (n % 2 == 1):
                n = 3*n+1
            else:
                n = n/2
            
            if powerof2(n):
                count += len(bin(n))-2
                break
            elif n in cache:
                count += cache[n]
                break
            else:
                count+=1
        cache[start] = count
    #    print('The answer is %d' %count)
    return cache
    
answer = Collatz(10**6)
test = list(answer.values())
final = test.index(max(test))+2 #adding three because we index from 2 on

print('The answer is %d' % final)
