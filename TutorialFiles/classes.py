class Dog():
    # attribute of class
    attOne='oneAtt'
    def __init__(self,breed,poww):
        self.breed=breed
        self.poww=poww


objectDog=Dog('something1','something2')
anotherdog=Dog('one','two')
# print("Class of Dog()"+str(objectDog))
# print("Class of Dog():arg1=> "+str(objectDog.breed)+" arg2=> "+str(objectDog.poww))
print('attOne:'+anotherdog.attOne+" Class of Dog():arg1=> "+str(anotherdog.breed)+" arg2=> "+str(anotherdog.poww))
