import random
Game = str(print( "\033[1m" +"WELCOME TO GUESS THE NUMBER"+ "\033[0m"))
str(print("\033[1m" +"SELECT WHICH GAMEMODE YOU WANT TO PLAY. "+ "\033[0m"))

Valid2 = "No"
while Valid2 == "No":
    try:
        GameMode_Selection = int(input("1 - Computer Guesses\n2 - You Guess\n3 - Exit\nEnter : "))
    except Exception:
        print("Enter 1/2/3 ONLY.")
    if GameMode_Selection >= 1 and GameMode_Selection <= 3:
        Valid2 = "Yes"

if GameMode_Selection == 1:
    Min = 1
    Max = 100
    Valid = "No"
    while Valid =="No":
        UserNumber = int(input("Enter a Number 1-100 : "))
        if UserNumber >= 1 and UserNumber <= 100:
            Valid = "Yes"

    UserInput = ""
    while UserInput != "Y":
        Computer_Guess = random.randint(Min,Max)
        print("Is the Number "+ " = " + str(Computer_Guess))
        UserInput = str(input("Type L For a Lower Guess, Type H for a Higher Guess, Type Y If the Answer is Correct : ")).lower()
        if UserInput == "l":
            Max = Computer_Guess
        if UserInput == "h":
            Min = Computer_Guess
        if UserInput == "y":
            print("O PANCHOD GUESS KR DITYAAAAAAAAAAAA O BANDARRRRRRRRRR!!!!!")
            break



if GameMode_Selection == 2:
    import random

    x = random.randint(1, 100)
    i = int(input("Guess the Number (1-100):"))
    while x >= i:
        print(f"Wrong! The Number is Greater than {i} ")
        i = int(input("Guess the Number (1-100):"))
    while x <= i:
        print(f"Wrong! The Number is Lesser than {i}")
        i = int(input("Guess the Number (1-100):"))
    while x == i:
        print("null")

    print(f"{i} is Correct!!!!!")

if GameMode_Selection == 3:
    print("Not Playing?, Exiting.")