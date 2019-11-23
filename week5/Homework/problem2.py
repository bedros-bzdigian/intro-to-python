def final_list(*argv1):
    b =[]
    y = make_list(*argv1)
    for f in y:
        if f % 2 == 0:
            continue
        else:
            b.append(f)
    print (b)        

def make_list(*argv):
    a = []
    for x in argv:
        a.append(x)
    return (a)

final_list(1,2,3,4,5,6,7,8,9)
