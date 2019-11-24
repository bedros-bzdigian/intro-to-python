class employee:
    def __init__(self,name,last_name,monthly_salary):
        self.name = name
        self.last_name = last_name
        self.__monthly_salary = monthly_salary

    def getfullname(self):
        return (self.name,self.last_name)

    def annualSalary(self):
        if self.__monthly_salary > 100:
            return "High"
        else:
            return "Low"

x = employee (name = "bedig",last_name = "bzdigian",monthly_salary = 120)   
print (x)          