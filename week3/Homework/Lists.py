a = [1 ,4 ,5 ,7, 8 ,-2 ,0 , -1]
print ("a[3]: " , a[3])
print ("a[5]: " , a[5])
tem = a 
tem.sort(reverse =True)
a_sorted = tem
print (a_sorted)
print ("The list a_sorted from 1..3: ", a_sorted[1:4])
print ("The list a_sorted from 2..6: ", a_sorted[2:7])
print ("the indice 2 from a_sorted: ", a_sorted [2])
print ("the indice 3 from a_sorted: ", a_sorted [3])
print ("a_sorted: ", a_sorted)
b = ["grapes" , "potatoes" , "tomatoes" , "orange" , "lemon" ,"broccoli" ,"carrot" , "sausages"]
tem1 = b
tem1.sort()
b_sorted = tem1
print (b_sorted)
c = a [1:4] + b[4:7]
print ("c: " , c)
