# Створіть декоратор retry який приймає першим аргументом число - кількість разів,
# яку потрібно буде повторити виконання функції у разі викидання нею помилки.
# (приклад можно знайти у презентації) (ValueError, TypeError)

def repeat(n):
    def decorator(func):
        def cycle(*args, **kwargs):
            for _ in range(n):
                try:
                    print("Start function")
                    result = func(*args, **kwargs)
                    print("End function")
                    return result
                except Exception as e:
                    print(f"Error: {e}")

        return cycle
    return decorator


@repeat(3)
def ba_bla():
    file = open(name_file, 'r')
    print(file.read())
    file.close()


name_file = "Import_thi.txt"
ba_bla()
