# Напишіть генератор, який фільтрує непарні числа з заданої послідовності.


def even_number_filter(n):
    for num in n:
        if num % 2 == 0:
            yield num


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = even_number_filter(number)

for i in even_nums:
    print(i)
