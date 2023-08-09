
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print("Animal:", self.name)
        print("Species:", self.species)


class Mammal(Animal):
    def __init__(self, name, species, diet_type):
        super().__init__(name, species)
        self.diet_type = diet_type

    def display_info(self):
        super().display_info()
        print("Diet type:", self.diet_type)


class Carnivore(Mammal):
    def __init__(self, name, species, diet_type, teeth_count):
        super().__init__(name, species, diet_type)
        self.teeth_count = teeth_count

    def display_info(self):
        super().display_info()
        print("Teeth Count:", self.teeth_count)


class Lion(Carnivore):
    def __init__(self, name, species, diet_type, teeth_count, mane_size):
        super().__init__(name, species, diet_type, teeth_count)
        self.mane_size = mane_size

    def display_info(self):
        super().display_info()
        print("Mane size:", self.mane_size)


lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

lion.display_info()
print("-" * 20)
carnivore.display_info()
print("-" * 20)
mammal.display_info()
