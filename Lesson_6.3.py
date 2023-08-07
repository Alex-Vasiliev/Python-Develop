# Розробіть клас "Car", який містить такі властивості:
# make (марка автомобіля), model (модель автомобіля),year (рік випуску автомобіля) і mileage (пробіг автомобіля).
# Забезпечте можливість доступу до цих властивостей через методи,
# а також зробіть властивості "make" і "model" приватними.
# Додайте метод "drive" до класу "Car", який збільшує пробіг автомобіля на задане значення.
# Перевірте, чи не перевищує пробіг заданий ліміт (наприклад, 300 000 км),
# і виведіть повідомлення про досягнення ліміту при спробі здійснити поїздку.

class Car:
    def __init__(self, make, model, year, mileage=0):
        self._make = make
        self._model = model
        self.year = year
        self.mileage = mileage

    def _get_make(self):
        return self._make

    def _get_model(self):
        return self._model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def drive(self, drive):
        limit = 300001
        if drive + self.mileage >= limit:
            print("Error:\n LIMIT EXCEEDED!\n maximum limit 300000")
        else:
            self.mileage += drive


car = Car("Toyota", "Rav-4", 2023)
print("Make -", car._get_make())
print("Model -", car._get_model())
print("Year -", car.get_year())
print("Mileage -", car.get_mileage())

car.drive(1)
car.drive(200000)
car.drive(99999)
print("Mileage =", car.mileage)
car.drive(1)
