class Animal:
    def __init__(self,animal):
        self.animal=animal
        print("I am" ,self.animal,"This is __init__!")

    def __str__(self):
        return f"class Animal have a single str {self.animal}!"

myanimal=Animal("cat")
print(myanimal)