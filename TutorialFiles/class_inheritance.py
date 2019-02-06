# base class
class Human():

    def __init__(self):
        print("human creared")

    def Eat(self):
        print("human eating")

    def Study(self):
        print("Studying")

#inheritace class
class Student(Human):

    def __init__(self):
        Human.__init__(self)
        print("student created")

    # overriding method
    def Eat(self):
        print("student eating")

# another class inheritance from student
class Instructor(Student):
    def __init__(self):
        Student.__init__(self)
        print("Instructor is created")

mystd=x()
mystd.Study()
mystd.Eat()
