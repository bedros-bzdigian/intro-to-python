def add_values(*argv1):
    list1 = ['Anna','Edgar']
    print ("List1 before changes: ",list1)
    x = add_list(*argv1)
    list1.append(x)
    print ("List1 after changes: ",list1)


    

    

def add_list(*argv):
    list0 = []
    for a in argv :
        list0.append(argv)
    return (list0)    

add_values(3,4,5,6,7,8,'n','v')