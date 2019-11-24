class police_car:
    def __init__(self,owner,price,pass_code,tax_value = 0.2):
        self.owner = owner
        self.price = price
        self.__pass_code = pass_code
        self.tax_value = 0.2

    def tax(self):
        return (self.price * self.tax_value)

    def greeting(self):
        if self.__pass_code == "admin":
            print ("Welcome to your car ", self.owner)
                          