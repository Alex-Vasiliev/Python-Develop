# Створіть ітератор, який перебирає всі паліндроми, з заданого списку слів.

class PalindromeIterator:
    def __init__(self, word_list):
        self.word_list = word_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.word_list):
            raise StopIteration
        word = self.word_list[self.index]
        word = word.lower()
        reversed_world = word[::-1]
        if reversed_world == word:
            self.index += 1
            return word
        else:
            self.index += 1
            return self.__next__()


world_list = ['level', 'racecar', 'python', 'madam']
palindrome_iter = PalindromeIterator(world_list)
for world in palindrome_iter:
    print(world)
