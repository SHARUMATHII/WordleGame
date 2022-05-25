import colorama 
from colorama import Fore,Style
import random
import sys

def read_random_word():
    with open("C:\\Users\ADMIN\\OneDrive\\Desktop\\Clone\\ValidWords.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array).lower()

print("Let's play Wordle:")
print("Type a 5 letter word below and press Enter. You have 6 tries to guess the random word. Using Colors you can able to guess it shortly.\n")

word = read_random_word()

for attempt in range(1,7):
    guess = input().lower()
    
    # overwrite the last line in the console
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

    # print colored letters
    for i in range(min(len(guess), 5)):
        if guess[i] == word[i]:
            print(Fore.GREEN+guess[i],end="")
        elif guess[i] in word:
            print(Fore.YELLOW+guess[i],end="")
        else:
            print(guess[i], end="")
    print()
    
    if guess == word:
        print("Congratulations! You guessed the word in %i guesses." %attempt)
    elif attempt == 6:
        print("You didn't guess the word within 6 tries, it was '%s'" %word)