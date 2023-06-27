# create a game "Field of Wonders"
import random

word_list1 = ["apple", "orange", "cherry", "dog", "cat", "sunshine", "blubbery", "ice", "cold"]
word_list2 = ["яблуко", "апельсин", "вишні"]
word_list = []
language = int(input("What language should the words be in? \n"
                     "Якою мовою мають бути слова? \n"
                     "1 - English\n"
                     "2 - Українська\n"
                     "\n"
                     "Enter your choiceВведіть ваш вибір: "))

if language == 1:
    word_list = word_list1

if language == 2:
    word_list = word_list2


def play_game(attempts):
    random_word = random.choice(word_list)
    guessed_letters = []
    guessed_word = ["*"] * len(random_word)

    print("Guess the word!")
    print("".join(guessed_word))

    while attempts > 0:
        input_letters = input("Your answer: ").lower()

        if input_letters == random_word:
            print("Congratulations, you guessed the word!")
            return

        elif len(input_letters) > 1:
            print("he word is not correct.")
            continue

        elif input_letters in guessed_letters:
            print("You have already entered this letter.")
            continue

        guessed_letters.append(input_letters)
        correct_gues = False

        for i, letters in enumerate(random_word):
            if input_letters == letters:
                guessed_word[i] = letters
                correct_gues = True

        print("".join(guessed_word))

        if "*" not in guessed_word:
            print("Congratulations, you guessed the word!")
            return
        if not correct_gues:
            print("There is no such letter.")
            attempts -= 1

    print("You lost The required word was: ", random_word)


number_of_attempts = int(input("Enter the number of attempts: "))
play_game(number_of_attempts)

