def sumDigits(n):
    #convert int to string
    test = str(n)
    
    #convert string to list
    test = list(test)
    
    #reconvert individual string to int
    test = map(int, test)
    
    #sum all those ints
    return sum(test)

print("The answer is %d" % sumDigits(2**1000))
