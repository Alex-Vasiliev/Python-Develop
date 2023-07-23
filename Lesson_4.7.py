# Створіть декоратор **`rate_limit`**,
# який обмежує кількість викликів декорованої функції протягом певного періоду часу.
# Декоратор повинен приймати два параметри `max_calls` та `period`.
# Перший параметр - максимальна кількість допустимих викликів функції.
# Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls` викликів.
# Вам допоможе модуль `datetime` для вирішення цієї задачі.

import datetime
from time import sleep


def rate_limit(max_calls, period):
    def decorator(func):
        list_time = []

        def wrapper(*args):
            if len(list_time) >= max_calls:
                print(f"Виклик функції привищує {max_calls} and {period}")
                return None

            list_time.append(datetime.datetime.now())

            func(*args)

        return wrapper
    return decorator


@rate_limit(max_calls=3, period=datetime.timedelta(seconds=10))
def say_hi(name):
    print("Hello: ", name)
    sleep(2)


say_hi("Alex")
say_hi("Alex")
say_hi("Alex")
say_hi("Alex")
say_hi("Alex")
say_hi("Alex")
