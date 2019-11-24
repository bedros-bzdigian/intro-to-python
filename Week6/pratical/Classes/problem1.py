class circle:
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color

    def getdesc(self):
        print ("A",self.color,"circle with radius",self.radius)

example = circle(12,"red")     
print (example)       