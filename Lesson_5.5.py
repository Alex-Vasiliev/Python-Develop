# Реалізуйте ітератор для перебору всіх ключів словника.
class DictKeysIterator:
    def __init__(self, dictionary_iter):
        self.dictionary_iter = dictionary_iter
        self.keys = list(dictionary_iter.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key_iter = self.keys[self.index]
            self.index += 1
            return key_iter
        else:
            raise StopIteration


dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
dict_iter = DictKeysIterator(dictionary)
for key in dict_iter:
    print(key)
