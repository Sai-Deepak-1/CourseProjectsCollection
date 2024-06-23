import random

class Dog:
    bark = "Woof Woof"

    def __init__(self,name) :
        self.luckyno = random.randint(1,100)
        self.name = name
        print("I'm a Dog "+name)

dog1 = Dog("Doggy")
dog2 = Dog("Oggy")

print(dog1.name,"Lucky Number is",dog1.luckyno,"and",dog2.name,"Lucky Number is ",dog2.luckyno)

# dog1.name = "Doggy"
# dog2.name = "Oggy"
print(dog1.name)
print(dog2.name)