'''
#The Fibonacci sequence is defined by the recurrence relation:
#
#
#
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

def fib(n):
    seq = [1,1,2]
    for i in range(3,n):
        seq[0],seq[1] = seq[1:]
        seq[-1] = sum(seq[:2]) 
        print(len(str(seq[-1])))
    return seq[-1]

test = fib(4782)

def fib_1000digits():
    seq = [1,1,2]
    index = 4
    while True:
        seq[0],seq[1] = seq[1:]
        seq[-1] = sum(seq[:2]) 
        if (len(str(seq[-1])) == 1000):
            break
        index+=1
    return index

answer = fib_1000digits()
