class MyZoo:
    def __init__(self,dic=None):
        if dic==None:
            self.animal={}
        else:
            self.animal=dic
        print("My Zoo!")

    def __str__(self):
        return f"{self.animal}"

    def __eq__(self, other):
        if(isinstance(other,MyZoo)):
            return self.animal.keys()==other.animal.keys()
        return False

    def __len__(self):
        return sum(self.animal.values())

myzoooo0 = MyZoo()
myzoooo1 = MyZoo({'pig':1})
myzoooo2 = MyZoo({'pig':5,'dog':3})
print(myzoooo1)
print(myzoooo2)
print(len(myzoooo2))
print(myzoooo1 == myzoooo2)