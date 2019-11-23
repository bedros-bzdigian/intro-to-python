def iter_num(n):
    n = int (n)
    for i in range (1,n):
        yield (i)
    


y = iter_num(66)
for i in y:
    print (next(y))       
