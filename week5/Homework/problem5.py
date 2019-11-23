def my_range (n):
    for x in range (0,n+1):
        yield (x)
print ("THere is no values left")

a = my_range(15)
print (next(a))