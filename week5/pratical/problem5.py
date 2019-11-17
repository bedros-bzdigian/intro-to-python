def func (name,*num):
    if len(num) == 0 :
        print ( name , "No grades available")   
    else:
        s = 0
        for x in num:
            s = s + x
        print (name,"your average grade is: ",s)    
x = 'Alex'
func (x)        

