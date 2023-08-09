
class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print("Car:", self.make, self.model)


class Sedan(Car):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print("Doors", self.doors)


class SUV(Car):
    def __init__(self, make, model, seats):
        super().__init__(make, model)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print("Seats:", self.seats)


class SportsCar(Car):
    def __init__(self, make, model, speed):
        super().__init__(make, model)
        self.speed = speed

    def display_info(self):
        super().display_info()
        print("Max speed:", self.speed)


# Створюємо об'єкти різних класів
sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

# Виводимо інформацію про кожен автомобіль
sedan.display_info()
print("-" * 20)
suv.display_info()
print("-" * 20)
sports_car.display_info()
