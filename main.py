import json
from typing import Type


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")


class Dog(Animal):
    def make_sound(self):
        return "bark"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Cow(Animal):
    def make_sound(self):
        return "moo"


class Rat(Animal):
    def make_sound(self):
        return "pipi"


class Alien(Animal):
    def make_sound(self):
        return "KILL"


def get_animal_instance(animal: str) -> (
        Type[Cow] | Type[Rat]
        | Type[Dog] | Type[Alien] | Type[Cat] | None
):
    animals = {
        "dog": Dog,
        "cat": Cat,
        "cow": Cow,
        "rat": Rat,
        "alien": Alien
    }
    return animals.get(animal, None)


with open('test.json', 'r') as file:
    data = json.load(file)

animal_name = data.get("animal")

if animal_name:
    animal_class = get_animal_instance(animal_name)
    if animal_class:
        animal = animal_class(animal_name)
        print(animal.make_sound())
    else:
        print("Unknown animal")
else:
    print("Animal field is missing")
