answer = input("What is your favorite color? ")

with open("user.txt", "w") as f:
    f.write(answer)

