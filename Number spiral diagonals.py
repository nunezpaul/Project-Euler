import numpy as np

def square(n):
    n=n /2
    square_array = np.ones((2*n+1,2*n+1))
    center = [n]*2
    for i in reversed(range(1,center[0]+1)):
        square_array[n-i,n+i] = (2*i+1)**2
        square_array[n-i,n-i] = (2*i+1)**2 - 2*i
        square_array[n+i,n-i] = (2*i+1)**2 - 4*i
        square_array[n+i,n+i] = (2*i+1)**2 - 6*i
    return square_array

test = square(1001)

def sum_diag(n):
    n= n/2
    square_array = np.ones((2*n+1,2*n+1))
    center = [n]*2
    sum = 1
    for i in reversed(range(1,center[0]+1)):
        sum += (2*i+1)**2
        sum += (2*i+1)**2 - 2*i
        sum +=(2*i+1)**2 - 4*i
        sum += (2*i+1)**2 - 6*i
    return sum


answer = sum_diag(1001)
