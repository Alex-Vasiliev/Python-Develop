# Змініть функцію even_odd_generator так, щоб вона генерувала послідовність чисел
# від 1 до n з рядками "Fizz" для чисел, які діляться на 3,
# "Buzz" для чисел, які діляться на 5, і "FizzBuzz" для чисел, які діляться як на 3, так і на 5.
# Приклад можливо подивитись у презентації до уроку


def even_odd_generator(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            yield f"{i} - FizzBuzz"
        elif i % 3 == 0:
            yield f"{i} - Fizz"

        elif i % 5 == 0:
            yield f"{i} - Buzz"


def key_user():
    inp_txt = input('Enter any key to continue: ')
    return inp_txt


enter_next = key_user()
# Створення генератора
my_generator = even_odd_generator(10000)

# Використання функції next() для отримання наступного значення
while enter_next:
    print(next(my_generator))
    key_user()

key_user()

