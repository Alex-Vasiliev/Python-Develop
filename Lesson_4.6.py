# Реалізувати декоратор кешування memoize, який кешує результати декорованої функції
# для покрашення продуктивності при повторних викликах тими самими аргументами.
# Тобто він повинен запам'ятовувати аргумент з якими функція визивалася і результат роботи функції з цими аргументами.
# І у випадку, якщо ми вже маємо результат,для цих аргументів,
# просто повернути закешований результат, замість виклику функції.

def memoize():
    cache = {}

    def decorator(func):
        def wrapper(*args):
            if args in cache:
                print(f"Result number {cache[args]}")
                return cache[args]
            else:
                result = func(*args)
                cache[args] = result
                return result
        return wrapper
    return decorator


@memoize()
def num(y, z):
    result = y + z
    print(f"Result number {result}")
    return result


num(3, 3)
num(3, 5)
num(3, 3)
num(4, 6)
num(3, 5)
