#Benson Chau
#Lab 8

import random

def FtoC():
    tF = float(input("What is the current temperature in Farenheit?"))
    tC = (tF-32)*5/9
    print("The temperature you said is ", tC, "degrees Celsius.")
#This is the funcion for option 5

def RPSLS():
    return random.randint(1,5)
#This is the function to pick out Sheldon's choice


name = input("Hello! Please type your name: ")
#menu_choice = 0
print("Hello ", name, "Welcome to Sheldon Cooper's mind. Here is your menu.\n1: Joke\n2: 15\n3: Quote\n4: Guess\n5: Temperature\n6: VS Sheldon")
menu_choice = int(input("Type the number of the option you want: "))
if (menu_choice==1):
    print("Bazinga!")
elif (menu_choice==2):
    for i in range(15):
        print(name, "\n")
elif (menu_choice==3):
    repitition = int(input("Pick a positive number:"))
    if (repitition<=0):
        print("I TOLD YOU TO PICK A POSITIVE NUMBER >:(")
        repitition = int(input("Pick a positive number:"))
    elif (repitition>0):
        for i in range(repitition):
            print("Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.\n")
elif (menu_choice==4):
    randnum = 17
    randguess = int(input("Guess a whole number between 0 and 100: "))
#    counter = 0
    while (randguess != randnum):
        if (randguess > 100 or randguess < 0):
            randguess = int(input("Please guess a number within 0 and 100, no more, no less: "))
        elif (randguess < randnum and randguess > -1):
            randguess = int(input("Incorrect! Your guess is too low. Guess again: "))
        elif (randguess > randnum and randguess < 101):
            randguess = int(input("Incorrect! Your guess is too high. Guess again: "))
    print("CORRECT! YOU GUESSED THE RIGHT NUMBER!!")
elif (menu_choice==5):
    FtoC()
elif (menu_choice==6):
    win = 0
    print("You must beat the mighty Sheldon Cooper in a game of Rock-Paper-Scissors-Lizard-Spock to escape. Good luck.\n")
    player_choice = int(input("Make a choice:\n1 represents Rock\n2 represents Paper\n3 represents Scissors\n4 represents Lizard\n5 represents Spock\n"))
    sheldon_choice = RPSLS()
    while (win == 0):
        if sheldon_choice == 1:
            if player_choice == 1:
                print("We both chose Rock.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 2:
                print("You won. Paper covers Rock.")
                win = 1
            elif player_choice == 3:
                print("I win. Rock crushes Scissors.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 4:
                print("I win. Rock crushes Lizard.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 5:
                print("You won, Spock vaporizes Rock.")
                win = 1
        elif sheldon_choice == 2:
            if player_choice == 1:
                print("I win. Paper covers Rock.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 2:
                print("We both chose Paper.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 3:
                print("You won, Scissors cuts Paper.")
                win = 1
            elif player_choice == 4:
                print("You won, Lizard eats Paper.")
                win = 1
            elif player_choice == 5:
                print("I win, Paper disproves Spock.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
        elif sheldon_choice == 3:
            if player_choice == 1:
                print("You won, Rock crushes Scissors.")
                win = 1
            elif player_choice == 2:
                print("I win, Scissors cuts Paper.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 3:
                print("We both chose Scissors.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 4:
                print("I win, Scissors decapitates Lizard.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 5:
                print("You won, Spock smashes Scissors.")
                win = 1
        elif sheldon_choice == 4:
            if player_choice == 1:
                print("You won, Rock crushes Lizard.")
                win = 1
            elif player_choice == 2:
                print("I win, Lizard eats Paper.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 3:
                print("You won, Scissors decapitates Lizard.")
                win = 1
            elif player_choice == 4:
                print("We both chose Lizard.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 5:
                print("I win, Lizard poisons Spock.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
        elif sheldon_choice == 5:
            if player_choice == 1:
                print("I win, Spock vaporizes Rock.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 2:
                print("You win, Paper disproves Spock.")
                win = 1
            elif player_choice == 3:
                print("I win, Spock smashes Scissors.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
            elif player_choice == 4:
                print("You win, Lizard poisons Spock.")
                win = 1
            elif player_choice == 5:
                print("We both chose Spock.")
                player_choice = int(input("Make a choice again: "))
                sheldon_choice = RPSLS()
        elif player_choice != 1 and player_choice != 2 and player_choice != 3 and player_choice != 4 and player_choice != 5:
            player_choice = int(input("Invalid choice. Make a choice again: "))
            sheldon_choice = RPSLS()

else:
    print("YOU DID NOT GIVE ME THE CORRECT INPUT\n")
    menu_choice = int(input("Type the number of the option you want: "))
