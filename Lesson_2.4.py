# Реалізуйте функцію, яка ділить два числа, але обробляє помилку **`ZeroDivisionError`**,
# якщо друге число дорівнює нулю.

num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    num_result = num1 / num2
    print(num_result)
except ZeroDivisionError:
    print("Введено невірні значення", "Числа на \"0\" не діляться", sep="\n")
except ValueError:
    print("Введенно не вірні значення", "Введіть числа!", sep="\n")
