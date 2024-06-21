import random


class Dog:
    bark = "Woof Woof"

    def __init__(self) :
        print("I'm a Dog ")
        self.luckyno = random.randint(1,100)

dog1 = Dog()
dog2 = Dog()

print("Dog 1 Lucky Num is ",dog1.luckyno," & Dog 2 Lucky Num is ",dog2.luckyno)

dog1.name = "Doggy"
# dog2.name = "Oggy"
print(dog1.name)
# print(dog2.name)