class Cat:
    def __init__(self, eat, talk, walk):
        self.eat = eat
        self.talk = talk
        self.walk = walk

    def eat(self):
        return "can eats a milk"
    def talk(self):
        return "can says meow"
    def walk(self):
        return "cat can run up to 20km/h"

class Dog:
    def __init__(self, eat, talk, walk):
        self.eat = eat
        self.talk = talk
        self.walk = walk

    def eat(self):
        return "dog eats a bone"
    def talk(self):
        return "dog says woof"
    def walk(self):
        return "dog can run up to 40km/h"

cat = Cat("milk", "meow", "20km/h")
dog = Dog("bone", "woof", "40km/h")

print("CAT:")
print(cat.eat())
print(cat.talk())
print(cat.walk())

print("\nDOG:")
print(dog.eat())
print(dog.talk())
print(dog.walk())