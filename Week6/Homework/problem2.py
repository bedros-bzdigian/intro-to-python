def div(x,y):
    try:
        x/y
        return x/y
    except Exception:
        print ("Can't divide")


a = div (4,1)
print (a)
b = div (4,0)
print (b)