t1 = (1,2,3,4,5,6)
print ("t1 before changes: " , t1)
x = t1[0:4] + ("hello",) + t1[5:]
print ("t1 after changes: " , x )
