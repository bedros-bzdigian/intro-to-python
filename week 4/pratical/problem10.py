num = [7,8,120,25,44,20,27]
print ("num before changes: ", num)
num = [x for x in num if x%2 != 0]
print ("num after changes: ", num)