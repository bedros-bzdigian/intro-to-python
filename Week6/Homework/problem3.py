class person:
    def __init__(self,name,last_name,age,gender,student,password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = bool(student)
        self.__password = password

    def Greeting(self,second_person):
        second_person = input ("please input a name: ")
        self.second_person = second_person
        print ("Welcome dear ",second_person)   

    def Goodbye(self):
        print ("Bye everyone!") 

    def Favourite_num(self,num1):
        num1 = input("please input a number:  ")
        self.num1 = num1
        print ("My favourite number is ",num1)

    def Read_file(self,filename):
        self.filename = filename
        filename = filename + '.txt'
        f = open(filename)
                
