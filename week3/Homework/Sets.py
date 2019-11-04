a1 = ["cookies" , "chocolate" , 8 , True , -3 , -5 , "chocolate" , 8 , False , 8]
b1 = [8 , True , 10 , 14 , "chocolate" , "milk" , "Jelly" , True , False , True]
set_a = set(a1)
set_b = set(b1)
print ("set_a: " , set_a)
print ("set_b:"  , set_b)
union_ab = set_a.union(set_b)
intersection_ab = set_a.intersection(set_b)
print("union_ab before changes: " , union_ab)
union_ab.add("kit-kat")
union_ab.add("oreo")
print ("union_ab after changes: " , union_ab)
new_set = union_ab | intersection_ab
print ("new_set: " , new_set)
"chocolate" in new_set
new_set.remove("oreo")
