# Створіть ітератор, який перебирає всі парні числа з заданого діапазону.

class EvenRangeIterator:
    def __init__(self, start_num, end_num):
        self.start_num = start_num if start_num % 2 == 0 else start_num + 1
        self.end_num = end_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_num > self.end_num:
            raise StopIteration

        result = self.start_num
        self.start_num += 2
        return result


even_nums = EvenRangeIterator(1, 10)
for num in even_nums:
    print(num)
