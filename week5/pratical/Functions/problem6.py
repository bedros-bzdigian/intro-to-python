def func(user,*value):
    if user == 'admin':
        y = 1 
        for x in value:
            print ("the argument",y, "name is: ",x) 
            y = y + 1        
    else:
        print ("access denied to the user X")
func('admin',4,5,6,"jj")