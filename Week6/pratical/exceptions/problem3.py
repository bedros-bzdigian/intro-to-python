list1 = ['a',0,2]
for a in list1:
    try:
        a = 1/a
        print (a)
    except:
        print ("Sorry, this value doesn't have a reciprocal")    