def py(a,b):
    return (a**2 + b**2)**0.5

a = range(1,500)
a.reverse()

for i in a:
    b = 400
    while b > 10:
        c = py(i,b)
        print(i+b+c)
        if c+i+b <= 1000:
            break
        else:
            b -=1
    if c+i+b == 1000:
        print(i*b*c)
        break

answer = i*b*c
