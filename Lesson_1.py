import random

word_list = ["apple", "banana", "orange", "kiwi", "pear"]


def play_game(attempts):
    random_word = random.choice(word_list)
    guessed_letters = []
    guessed_word = ["*"] * len(random_word)

    print("Відгадайте слово!")
    print(" ".join(guessed_word))

    for _ in range(attempts):
        user_input = input("Ваша відповідь: ").lower()

        if user_input == random_word:
            print("Вітаю, ви вгадали слово!")
            return

        if len(user_input) > 1:
            print("Слово не правильне.")
            continue

        if user_input in guessed_letters:
            print("Ви вже ввели цю літеру.")
            continue

        guessed_letters.append(user_input)
        correct_guess = False

        for i, letter in enumerate(random_word):
            if user_input == letter:
                guessed_word[i] = letter
                correct_guess = True

        print(" ".join(guessed_word))

        if "*" not in guessed_word:
            print("Вітаю, ви вгадали слово!")
            return

        if not correct_guess:
            print("Такої літери немає.")

    print("Ви програли. Загадане слово було:", random_word)


number_of_attempts = int(input("Введіть кількість спроб: "))
play_game(number_of_attempts)
