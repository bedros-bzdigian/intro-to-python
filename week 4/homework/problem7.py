list4 = [[10,20,40], [40,50,60] , [70,80,90] ]
list5 = list4.copy()
for x in range (0,3):
    list5[x][2] = 100
print ("list4 ", list4)
print ("list5 ", list5)