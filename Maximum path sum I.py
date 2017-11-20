with open('path to file') as f:
    test = f.readlines()
    
for i,j in enumerate(test):
    test[i] = j.replace('\n', '')
    test[i] = test[i].split(' ')
    test[i] = map(int, test[i])

for i in reversed(range(len(test)-1)):
    for j in range(len(test[i])):
        
        if test[i+1][j] > test[i+1][j+1]:
            test[i][j] += test[i+1][j]
        else:
            test[i][j] += test[i+1][j+1]
        
print(test[0][0])
