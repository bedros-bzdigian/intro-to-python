y = list(input("please input a list: "))
def list_even(x):
    x = list(x)
    s = 0 
    for check in x:
        if int(check) % 2 == 0 :
            s = s + 1
    print ("The number of even values in your list is: ",s)        


list_even(y)      