t1 = (1, True , 'a' , -2 , 'Anna')
t1 = (1,) + t1[2:]
print (t1)
t2 = (1,2,3,4,5)
t3 = t1[0:2] + t2[0:3]
print (t3)
print ("The value of the index 2 from t3: " , t3[2])
t4 = [(1,3,5) , (8,9) , ("Anna" , "Bob" , "Alice")]
print (t4[0][1])