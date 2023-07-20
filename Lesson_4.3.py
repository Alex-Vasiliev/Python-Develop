# Створіть простий декоратор логування log_func,
# який буде прінтити будь яке повідомлення перед визовом декорованої функції, та після.


def log_func(func):

    def processing():
        print(30 * '*')
        print(f"START FUNCTION: '{func.__name__}'")
        func()
        print(f"END FUNCTION: '{func.__name__}'")
        # print(30 * '*')

    return processing


@log_func
def say_hi():
    print("Hello")


@log_func
def say_by():
    print("By")


say_hi()
say_by()
