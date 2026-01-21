#Benson Chau
#Lab 9
#GitHub test comment

print("     Menu     ")
print("______________")

def FtoC():
    tF = float(input("What is the current temperature in Farenheit?"))
    tC = (tF-32)*5/9
    print("The temperature you said is ", tC, "degrees Celsius.")
#This is the funcion for option 5

name = input("Hello! Please type your name: ")
#menu_choice = 0
print("Hello ", name, "Welcome to Sheldon Cooper's mind. Here is your menu.\n1: Joke\n2: 15\n3: Quote\n4: Guess\n5: Temperature\n")
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
#            counter = counter + 1
elif (menu_choice==5):
    FtoC()
#    print("The temperature you said is ", tC, "degrees Celsius.")

else:
    print("YOU DID NOT GIVE ME THE CORRECT INPUT\n")
    menu_choice = int(input("Type the number of the option you want: "))
