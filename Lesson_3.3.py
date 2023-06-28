# Розробіть клас Vehicle для представлення транспортного засобу. Додайте атрибути,
# такі як назва, швидкість і вартість. Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю.
# Створіть список транспортних засобів і відсортуйте його за швидкістю.
class Vehicle:

    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        return self.speed > other.speed


vehicles = [
    Vehicle("Car", 250, 10000),
    Vehicle("Bicycle", 30, 500),
    Vehicle("Motorcycle", 200, 8000),
    Vehicle("Bus", 100, 20000)
]

sorted_vehicles = sorted(vehicles, key=lambda vehicle: vehicle.speed)

for vehicle in sorted_vehicles:
    print(vehicle.name, vehicle.speed, vehicle.cost)
