#!/usr/bin/env python3

class Person:
    def __init__(self, name) -> None:
        self.name = name


guido = Person("Guido")

print(guido.name)