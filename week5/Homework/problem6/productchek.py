products = {"candy":10 , "juice":5, "pen":50}

def check(product,name):
    product = str (product)
    if (product  in products) and (name == products[product]):
        return True
    else :
        return False


a = check("candy",10)
print (a)