name = str(input("please enter your name! "))
print ("Welcome Mr. ",name)
age = int (input ("please enter your age! "))
password = str (input ("please enter your password! "))
if age < 16:
    print ("Dear ",name,", you are too young to register")
x = ('*' in password ) or ('&' in password )
if not x :
    print ("please enter a different password ")
