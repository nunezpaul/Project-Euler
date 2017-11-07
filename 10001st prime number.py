from functools import partial

def check(prime_check, prime):
    return not prime_check%prime == 0

dict_prime = {2,3,5}

counter = 3
prime_check = max(dict_prime)+2

while True:
    test = map(partial(check, prime_check), dict_prime)
    if all(test):
        dict_prime.add(prime_check)
        counter +=1

    prime_check += 2
    
    if counter == 10001:
        break
    
test = list(dict_prime)
test.sort()

answer = test[-1]
