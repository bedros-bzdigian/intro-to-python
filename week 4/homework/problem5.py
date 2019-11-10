menu = ["ice cream" , "chocolate" , "apple crisp" , "cookies"]
desert = str (input("please enter a desert: "))
if desert in menu:
    print ("your desert will arrive in 10 minutes")
else:
    print("please choose another desert") 
while not (desert in menu):
    desert = str (input("please enter a desert: "))
    if desert in menu:
        print ("your desert will arrive in 10 minutes")
        break
