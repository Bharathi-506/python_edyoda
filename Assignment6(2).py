class Dog:
    def __init__(self, name, age,coat):
        self.name = name
        self.age = age
        self.coat = coat


def sayHi(dog):
    print(f'Hi, my name is {dog.name} and I am {dog.age} years old! coated with {dog.coat}')

d1 = Dog('JackRussellTerrier', 4, 'Black')
d2 = Dog('bulldog', 3 , 'White')

sayHi(d1) 
sayHi(d2) 