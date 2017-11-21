def sorted_names():
    with open('path to file/p022_names.txt') as f:
        names = f.readlines()[0]
        
    test = names.split(',')
        
    for i in range(len(test)):
        test[i] = eval(test[i])
        
    test.sort()
    return test


def char2num(char):
    return ord(char)-(ord('A')-1)

def sumNameScores(names):
    namescore = [0]*len(names)
    
    index = 1
    for name in names:
        test = list(name)
        namescore[index-1] = sum(map(char2num, test))
        namescore[index-1] = namescore[index-1]*index
        index+=1
    
    return sum(namescore)


names = sorted_names()
answer = sumNameScores(names)
