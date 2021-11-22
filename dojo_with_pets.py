class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f'Walking {self.first_name} {self.last_name}.')
        return self

    def feed_treat(self):
        print(f'Feeding {self.first_name} {self.last_name} {self.treats}.')
        return self

    def feed_pet_food(self):
        print(f'Feeding {self.first_name} {self.last_name} {self.pet_food}.')
        return self

    def bathe(self):
        print(f'Bathing {self.first_name} {self.last_name}.')
        return self

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    def sleep(self):
        print(f'{self.name} is sleeping.')
        return self

    def eat(self):
        print(f'{self.name} is eating.')
        return self

    def play(self):
        print(f'{self.name} is doing a {self.tricks}.')
        return self

    def noise(self):
        print(f'{self.name} is making noise.')
        return self

# nibbles = Ninja("Nathaniel", "Nibbles", "Cookies", "Kitty Chow", "Cat")
nibbles = Pet("Nibles", "Cat", "cart wheel")

# nibbles.walk().feed_treat().feed_pet_food().bathe()
nibbles.sleep().eat().play().noise()

