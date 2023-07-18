# Створіть контекстний менеджер DividerContext, який буде прінтити символ,
# який ми до нього передамо як розділитель для основного блоку коду до та після його виконання.
# Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.

from contextlib import contextmanager
user_symbol = input("Please enter a symbol: ")


@contextmanager
def divider_context(symbol):

    def enter_symbol():
        print(30 * symbol,)

    enter_symbol()
    yield
    enter_symbol()


with divider_context(user_symbol):
    # Блок коду, що виконується в контексті
    print("Decorator - Inside the context")


class DividerContext:
    def __init__(self, symbol):
        self.symbol = symbol

    def __enter__(self):
        # Виконання певних дій перед входом в контекст
        print(30 * self.symbol)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Виконання певних дій перед виходом з контексту
        print(30 * self.symbol)


with DividerContext(user_symbol):
    # Блок коду, що виконується в контексті
    print("Class - Inside the context")
