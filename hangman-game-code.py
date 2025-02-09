import random as rd
import time
import os
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========          

''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========

''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''']
def pick_random_word(ch):
    word_dict = {
        "Animal": ["lion", "tiger", "bull", "monkey", "cow", "panda"], 
        "Bird": ["sparrow", "crow", "peacock", "eagle", "parrot"],
        "Cartoon": ["shinchan", "doremon", "hattori"]
    }
    key1 = list(word_dict.keys())[ch - 1]
    word = rd.choice(word_dict[key1])
    return key1, word

def start():
    print("\nAre you ready to play?\n1. Animal\n2. Bird\n3. Cartoon")
    ch = int(input("Choose your interest: "))
    
    if ch not in [1, 2, 3]:
        print("Invalid choice! Please restart the game and select a valid option.")
        start()

    key1, word = pick_random_word(ch)
    life = 7
    print("Total lives:", life)
    guessed_word = ["_"] * len(word)
    print("Hint:", key1)
    print(' '.join(guessed_word))
    guessed_letter = set()
    
    while life > 0 and "_" in guessed_word:
        letter = input("Guess: ").lower()
        if letter in guessed_letter:
            print("Letter already used")
        elif letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word[i] = letter
            print("Life left:", life)
            print(' '.join(guessed_word))
            guessed_letter.add(letter)
        else:
            print("Wrong guess")            
            print(stages[7 - life])
            life -= 1            
            print("Life left:", life)
            print(' '.join(guessed_word))

    if "_" not in guessed_word:
        print("You won!")
        frame_0 = """
                   +---+ 
                       | 
                   O   | 
                  /|\\  | 
                  / \\  | 
                       | 
                =========
                """

        frame_1 = """
                   +---+ 
                       | 
                  \\O/  | 
                   |   | 
                  / \\  | 
                       | 
                =========
                """

        for _ in range(6):  # Loop for 6 frames (3 up-down cycles)
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            print(frame_0)
            time.sleep(0.5)  # Pause for 0.5 seconds

            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            print(frame_1)
            time.sleep(0.5)
    else:
        print("You lose. The word was:", word)
    
    con = input("Do you want to continue('y' or 'n'): ")
    if con == 'y':
        start()
    else:
        exit

start()
