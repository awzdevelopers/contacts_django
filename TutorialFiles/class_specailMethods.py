# special methods __init__ and __str__
class contacts():
    def __init__(self,name,family,phoneNum):
        self.name=name
        self.family=family
        self.phoneNum=phoneNum

    def __str__(self):
        return "Name: {}, Family: {}, phone: {} ".format(self.name,self.family,self.phoneNum)

    def __len__(self):
        return self.phoneNum


cont=contacts("ali","alavi","0916916666")
print(str((cont.__len__())))

mylist=[1,2,3,4,5,6]

# print(len(mylist))
