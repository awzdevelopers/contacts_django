
#  http://python.coderz.ir/
list=[1,2,3,4,5]
list.append(6)
print(list)

tuple=(1,2,3)

dic={'key1':'A','key2':'B'}
print(dic['key1'])

class Human():
    print("human class")

    def walking(self):
        print("human is walking")

class contact(Human):
    print("contact is creating")

    def __init__(self,name,family,address):
        self.name=name
        self.family=family
        self.address=address

    def __str__(self):
        return self.name+" / "+self.family+" / "+self.address

contact1=contact(name="omid", family="hamidi", address="ahvaz")
contact1.walking()
print(contact1)
