'''
d(220) = 284
factors: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110

d(284) = 220
factors: 1, 2, 4, 71 and 142
'''

def factors(n):    
    hold = (list([i, n//i] for i in range(1, int((n**0.5)) + 1) if n % i == 0))
    hold = [item for sublist in hold for item in sublist]
    hold.sort()
    return hold[:-1]
    
def check_amicable(n):
    test1 = sum(factors(n))
    test2 = sum(factors(test1))
    return test2 == n

def sum_of_amicables(end):
    sum_nums = 0
    #amicable_nums under 10**5
    for i in range(1,end):
        test1 = check_amicable(i)
        test2 = sum(factors(i))<end
        test3 = i !=sum(factors(i))
        if test1 and test2 and test3 :
            sum_nums += i
    return sum_nums

#The answer is:
sum_of_amicables(10**4)
