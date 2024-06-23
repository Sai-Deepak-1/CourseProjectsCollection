import random


class Animal:
    info = "I am an Animal"

    def __init__(self, name):
        self.name = name
        print("An Animal is Created")

class Dog(Animal):
    info = "I am a Dog"

    def __init__(self, name):
        super().__init__(name)
        self.luckyno = random.randint(1, 100)
        print("I'm a Dog " + name)

    def bark(self):
        print(f"Dog's name is {self.name} and lucky no is {self.luckyno}")

class Bulldog(Dog):
    info = "I am a Bulldog"

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        print("An Bulldog is Created")

# dog1 = Dog("Doggy")
dog1 = Bulldog("Doggy")

print(dog1.info)
