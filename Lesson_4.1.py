# Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду.
# Контекстний менеджер повинен виводити час, що минув, при виході з контексту.
# Використовуйте контекстний менеджер для вимірювання часу виконання певного фрагменту коду.
# Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.

from time import time, sleep
from contextlib import contextmanager


@contextmanager
def timer():
    # Виконання певних дій перед входом в контекст
    print("Decorator - Entering the context")
    try:
        # Виконання блоку коду в контексті
        start = time()
        yield
        end = time()
        elapsed_time = round(end - start, 3)
        print(f"*** Function time: {elapsed_time} ***")
    finally:
        # Виконання певних дій перед виходом з контексту
        print("Decorator - Exiting the context")
        print(40 * "|")


with timer():
    # Блок коду, що виконується в контексті
    sleep(3)
    print("Decorator - Inside the context")


class Timer:

    def __enter__(self):
        # Виконання певних дій перед входом в контекст
        print("Class - Entering the context")
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Виконання певних дій перед виходом з контексту
        end = time()
        elapsed_time = round(end - self.start, 3)
        print(f"*** Function time: {elapsed_time} ***")
        print("Class - Exiting the context")


with Timer():
    # Блок коду, що виконується в контексті
    sleep(3)
    print("Class - Inside the context")

# ground = time()
# broun = Timer()
# with ground, broun:
#     pass
