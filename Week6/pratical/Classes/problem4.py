class car:
    def __init__(self,model,color,max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed
    def comparecar(self,car2):
        if car2.max_speed > car1.max_speed:
            return ("car2 is better than car1")
        else:
            return ("car1 is better than car2")

car1 = car (max_speed = 13,model = 2019, color = "red")
car2 = car (max_speed = 12,model = 2019, color = "red")

