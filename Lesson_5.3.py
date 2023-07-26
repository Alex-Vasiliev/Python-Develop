# Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде повертати наступний символ рядку.

class String:
    def __init__(self, txt):
        self.current = txt
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.current):
            value = self.current[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


string = "Hello, World!"
str_iter = String(string)
for char in str_iter:
    print(char)
