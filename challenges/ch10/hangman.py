import random

words = ["cat",  "dog",  "bird",  "beast",  "bat"]

def hangman(word):
    wrong = 0
    stages = ["", 
                   "________        ", 
                   "|       |       ",
                   "|       |       ", 
                   "|       0       ", 
                   "|      /|\      ", 
                   "|      / \      ", 
                   "|               "
                   ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    
    print(("My word is: " + " ".join(board)))
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(("My word is: " + " ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
            
    if not win:
       print("\n".join(stages[0: wrong]))
       print("You lose! It was {}.".format(word))

hangman(words[random.randint(0,  5)])
  
