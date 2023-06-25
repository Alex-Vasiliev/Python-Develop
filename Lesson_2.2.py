# Створіть функцію, яка приймає два числа від користувача та обробляє помилку, якщо введені дані не є числами.

number1 = input("Enter your number-1: ")
number2 = input("Enter your number-2: ")

try:
    num1 = int(number1)
    num2 = int(number2)
    print(number1, number2, sep="\n")
except ValueError:
    print("Невірно введено данні. Введіть числа!")
