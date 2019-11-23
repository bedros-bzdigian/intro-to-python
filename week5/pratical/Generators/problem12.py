def power (x):
    for i in range (0,x+1):
        a = 2 ^ i
        yield (a)
        print (next (a))

y = power (4)
for a in range (0,5):
    print (next(y))