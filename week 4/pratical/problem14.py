a = ['a','abc','xyz','s','aba','1221']
s = 0 
for x in range (0,6):
    if (len(a[x]) >= 2) and (a[x][0] == a[x][len(a[x]) - 1]):
        s = s + 1
print (s)      