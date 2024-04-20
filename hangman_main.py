import random

#print welcome message
print ("""
                 WELCOME TO
   _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \ 
 ( H ) ( A ) ( N ) ( G ) ( M ) ( A ) ( N )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
       
                   by AJ 

""")
#print instructions
print ("""
This program will select a word at random and you will guess letter by letter, what the word is.
You do not need to guess multiple of the same letter.
You will have 11 lives.
""")

#function to start the game if conditions are met
def initialise_word_for_game():
    '''open file as read only and assign to variable "file"'''
    with open("word_list.txt", "r") as file:
        #print the contents of the file
        possible_words = (file.read().split())
    #assign the game_word variable to a random word in the list possible_words
    game_word = random.choice(possible_words)

    game_start(game_word)

def game_start(game_word):
    '''function for when the game starts'''
    lives = 11
    guessed_counter = 0
    print("The word you need to guess has ", len(game_word), " letters")
    guessed_preview = ("_"*(len(game_word)))

    while guessed_counter < (len(game_word)) and lives > 0:
        current_letter = input("Please guess a letter: ")
        sanitised_letter = current_letter.lower()
        letter_found = False
        for i in range(len(game_word)):
            if sanitised_letter == game_word[i]:
                guessed_counter += 1
                letter_found = True
                print("Correct!")
                guessed_preview = guessed_preview[:i] + sanitised_letter + guessed_preview[i+1:]

        print("Guessed word so far: ", guessed_preview,"\n")

        if not letter_found:
            print("Wrong! Please try again.")
            lives -= 1
            print("Lives left: ", lives)         
    if guessed_counter == (len(game_word)):
        print ("Well Done! You guessed the word correctly! Word guessed: ", game_word)
    else:
        print("Sorry, word not guessed. The word was: ", game_word)

def is_user_ready():
    '''code for asking if the user is ready to start the game'''
    ready_or_not = input("Are you ready? (y/n): ")

    if ready_or_not in ["y","Y","yes","Yes","YES"]:
        initialise_word_for_game()

    elif ready_or_not in ["n","N","no","No","NO"]:
        print("Fair enough bud.")
        print("Exiting.........")
        exit()
    else:
        print ("Sorry didn't catch that. Try Again.")
        is_user_ready()

is_user_ready()
