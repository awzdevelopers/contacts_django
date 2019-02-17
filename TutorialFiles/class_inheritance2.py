# base class
class Human():

    def __init__(self,name):
        print("human creared,Hi "+name)

    def Eat(self):
        print("human eating")

    def Study(self,name):
        print("Studying :"+name)

class Ehsan(Human):
    def Bye(self):
        print("Bye ")


ehsan1=Ehsan(name="ehsan")
ehsan1.Bye()
ehsan1.Study("ehsan")
