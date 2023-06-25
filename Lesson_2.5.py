# Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.

file = open("Import_this.txt")
count_result = 0


def count_words(sentence):
    words = sentence.split()
    return len(words)


for word in file:
    count = count_words(word)
    count_result += count
    print(word)
file.close()
print("Кількість слів у тексу: ", count_result)

