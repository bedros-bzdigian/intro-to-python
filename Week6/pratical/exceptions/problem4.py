username = str(input("pleas input a name:  "))
try:
    if username == "rambo":
        raise Exception
except Exception:
    print ("Rambo is an invalid username")
else:
    print ("Welcome ",username)    