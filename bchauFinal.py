#Benson Chau
#Final Question 1

print("Hello!\n")
choice = float(input("Pick one of the following options:\n1 - Joke\n2 - Food\n3 - Guess\n"))
if choice == 1:
    name = input("What is your name? ")
    print("*knocks* *knocks* *knocks* ", name, " *knocks* *knocks* *knocks* ", name, " *knocks* *knocks* *knocks* ", name)
if choice == 2:
    for i in range(1, 21):
        print("Pizza\n")
if choice == 3:
    guess = float(input("Guess a number: "))
    while guess != 0:
        guess = float(input("You guessed wrong. You are stuck until you guess the correct number. Guess a number again: "))
if choice != 1 and choice != 2 and choice != 3:
    choice = float(input("You did not make a correct selection. Pick one of the following: "))


