import random

def play_hangman():
    word_list = ["python", "hangman", "programming", "developer", "algorithm", "debugging", "function", "variable", "syntax", "loop"]
    word = random.choice(word_list).lower()
    guessed = set()
    attempts = 10
    name =input('Enter name of user: ')
    print("Welcome to Hangman," + name + "!")



    while attempts > 0:
        display_word = ''.join([letter if letter in guessed else '_' for letter in word])
        print(f"Word: {display_word}")
        
        if '_' not in display_word:
            print(f"Congratulations! You've guessed the word '{word}'!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"'{guess}' is not in the word. Attempts left: {attempts}")

    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()