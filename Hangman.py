import random

def hangman():
    words = ["python", "programming", "computer", "science", "algorithm"]
    secret_word = random.choice(words)
    word_letters = set(secret_word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    attempts = 5

    while len(word_letters) > 0 and attempts > 0:
        print("You have", attempts, "attempts remaining.")
        print("Used letters:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in secret_word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                attempts -= 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if attempts == 0:
        print('You ran out of attempts. The word was', secret_word)
    else:
        print('Congratulations! You guessed the word', secret_word, 'correctly!')

hangman()