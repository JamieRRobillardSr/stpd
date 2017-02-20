numbers = [100,  34,  23,  34,  54,  23,  56,  34]
i = 0

while True:
    answer = input("Guess which number I have thinking of or 'q' to quit: ")
    if answer == "q":
        break
    if int(answer) == numbers[i]:
        print("You guessed my number correct!\n")
    else:
        print("You did not guess my number.\n")

    i += 1
    if i > 7 :
        i = 0;
    
