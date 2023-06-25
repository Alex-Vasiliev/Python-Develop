# Обробіть виняток IndexError, коли програма намагається отримати
# доступ до неправильного індексу в списку.

list_1 = [1, 2, 3, 4, 5]

try:
    index = 6
    value = list_1
    print(value[index])
except IndexError:
    print("Помилка, невірно введенний індекс")
