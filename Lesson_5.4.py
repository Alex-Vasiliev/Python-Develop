# Напишіть генератор, який видає послідовність квадратів чисел від 1 до N.

def square_generator(n):
    for num in range(1, n+1):
        result = num * num
        yield result


for square in square_generator(10):
    print(square)
