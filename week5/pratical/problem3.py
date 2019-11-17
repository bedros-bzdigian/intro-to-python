def password(x):
    x = str(x)
    s = 0 
    for y in x:
        if (y == '1' or y == '2' or y == '3' or y == '4' or y == '5' or y == '6' or y == '7' or y == '8' or y == '9' or y == '0'):
            s = s + 1
    if ((len(x) > 9) and (s > 1))  :
        print (True)
    else:
        print (False)         
            
f = 'gthbfe45'
password(f)