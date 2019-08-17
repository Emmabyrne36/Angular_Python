import random
import sys

# For loops
for x in range(0, 10):
    print(x, ' ', end="")

# Random number
random_num = random.randrange(0, 100)
print(random_num)

# User input
# name = sys.stdin.readline()
# print("Hello ", name)

# Files
# test_file = open("test.txt", "wb")
# print(test_file.mode)
# print(test_file.name)
# test_file.write(bytes("Write me to the file\n", "UTF-8"))
# test_file.close()

# OOP
class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    # Create getters and setters for all other properties (not included here)

    def get_type(self):
        print(self)

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

cat = Animal("Whiskers", 30, 4, "Meow")
print(cat.toString())

class Cat(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Cat, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def toString(self):
        return super().toString() + " and has owner " + self.__owner

cat2 = Cat("Whiskers", 30, 4, "Meow", "Jane Doe")
print(cat2.toString())
cat.get_type()
cat2.get_type()