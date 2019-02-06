class Circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def setRadius(self,newR):
        self.radius=newR

circle1=Circle(2)
# changing the pi
# circle1.radius=122
circle1.setRadius(122)
print(circle1.area())
