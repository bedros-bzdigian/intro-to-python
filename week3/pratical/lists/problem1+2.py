import sys

list1 = ["hello" , 1 ,True]
print ("list1 before adding: " , list1)

list2 = sys.argv[1:]

print ("list1 after adding: " , list1 + list2 )
