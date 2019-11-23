def Text ():
    b =  "Hi everyone"
    x = make_lower("Hi everyone")
    x = add_text("Hi everyone")
    return (x)

def make_lower (x):
    x = str(x)
    x.lower()
    return x

def add_text (y):
    y = str(y)
    y = y + "!!! Welcome to the party"
    return (y)
print (Text ())
