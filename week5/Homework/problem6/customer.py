from productchek import check 
def main (product,num,price):
     def buy(product,num,price):
        a = check(product,num)
        if a == True :
            print ("You bought",product,"and spent",num*price)
        else:
            print ("Sorry! We are out of the product")
                

main("candy",11,3)