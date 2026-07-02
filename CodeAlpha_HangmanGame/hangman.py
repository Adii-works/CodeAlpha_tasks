import random

def hangman():
    words = ["apple", "python", "laptop", "coding", "banana"]

    word = random.choice(words)
    guessed = []
    chances = 6

    print("Welcome to Hangman Game!")

    while chances > 0:
        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        if "_" not in display:
            print("You Win!")
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed:
            print("Already guessed.")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!")
        else:
            chances -= 1
            print("Wrong! Chances left:", chances)

    if chances == 0:
        print("You Lost!")
        print("The word was:", word)

hangman()