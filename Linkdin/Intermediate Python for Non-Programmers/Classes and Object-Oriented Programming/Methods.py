import random


class Dog:
    bark = "Woof Woof"

    def __init__(self, name):
        self.name = name
        self.luckyno = random.randint(1, 100)
        print("I'm a Dog " + name)

    def bark(self):
        print(f"Dog's name is {self.name} and lucky no is {self.luckyno}")


dog1 = Dog("Doggy")
dog2 = Dog("Oggy")

dog1.bark()
dog2.bark()