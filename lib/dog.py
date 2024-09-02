#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed='Mutt') -> None:
        self.name = name
        self.breed = breed

dog = Dog('Fido', 'Dalmatian')

print(dog.name)
print(dog.breed)