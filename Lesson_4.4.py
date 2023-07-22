# Реалізувати декоратор timeit, який вимірює час виконання декорованої функції і виводить його.
# Для отримання часу роботи скористуйтесь модулем time і функцією time.time()
import time
from time import sleep


def timeit(func):

    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print(f"Function execution time:\n-{func.__name__}-\n{finish - start} sec.")
    return wrapper


@timeit
def say_hi():
    sleep(1)
    print("Hello")


say_hi()
