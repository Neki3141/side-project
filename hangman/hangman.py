import os
import random

#DEFINATION 
HANGMANPICS = ['\n\n','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# SELECT MODE AND RETURN WORD IN THAT MODE
def select_level(mode):
    match mode:
        case 'e':
            num = random.randint(0,14)
            filename = "easy.txt"
        case 'm':
            num = random.randint(0,14)
            filename = "med.txt"
        case 'h':
            num = random.randint(0,14)
            filename = "diff.txt"
        case _:
            num = random.randint(0,14)
            filename = "xdiff.txt"
    
    file = open(filename, "r")
    line = file.readlines()
    return line[num]

# PRINT GUESS LINE WITH CHAR AND MISSING CHAR
def print_guess_line():
    for letter_print in guess_buffer:
        print("." + letter_print, end='')
    print(".")


# MAINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN:
os.system('clear')
print("WELCOME TO HANGMAN")
print("There are 3 levels: EZ, MED, HARD")

# VALIDATE INPUT FOR ENTERING GAME
level = input("choose level (e, m, h, s): ")
#level = 'e'
while level != 'e' and level != 'm' and level != 'h' and level != 's':
    print("Choose again my little buddy")
    level = input("choose level (e, m, h, s): ")

# GENERATE KEY WORD
word_key = select_level(level)
word_key = word_key.upper()
print(word_key)
letter_count = len(word_key) - 1

# VARIABLE FOR HANGMAN
lose_condition = 0
win_condition = 0
alphabelt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
guess_buffer = ['_']*letter_count

# ENTERING GAME
while lose_condition < len(HANGMANPICS) and win_condition != letter_count:
    print(alphabelt)
    
    # VALIDATE INPUT
    while True:
        letter_guess = input("Guess 1 letter: ")
        if len(letter_guess) == 1 and letter_guess.isalpha(): break
        print("Invalid input bro")
    letter_guess = letter_guess.upper()
    
    
    # CHECKING IF THE LETTER ALR TRIED
    if alphabelt.find(letter_guess) == -1:
        print("You already try that letter")
        continue

    # GOING TO MAIN LOGIC
    else:
        # CLEAR SCREEN FOR BETTER OUTPUT
        os.system('clear')  # For macOS/Linux
        alphabelt = alphabelt.replace(letter_guess,'*')
        
        # PRINT CHAR WITH LINE
        print("Guessed char: ", end='')
        
        # SAVE LETTER GUESS BUFFER AS A STRING
        if word_key.find(letter_guess) != -1:
            for i in range (0,letter_count):
                if letter_guess == word_key[i]:
                    guess_buffer[i] = letter_guess
                    win_condition += 1
            print("CORRECT")
            print_guess_line()
        else:
            lose_condition += 1
            print("WRONG LETTER: " + letter_guess)
            print_guess_line()
        
        print(HANGMANPICS[lose_condition])



# CHECK WIN/LOSE CONDITION
if win_condition == letter_count:
    print("Just lucky this time :)")
else:
    print("Loser!")

