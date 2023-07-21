import random
Game = str(print( "\033[1m" +"WELCOME TO GUESS THE NUMBER"+ "\033[0m"))

str(print("\033[1m" +"SELECT WHAT GAMEMODE YOU WANT TO PLAY. "+ "\033[0m"))
GameMode_Selection = int(input("Press 1 to make computer guess your Number, "
                      "Press 2 For you to Guess Computers Number,"
                      " Press 3 to Exit : "))

if GameMode_Selection == 1:

 UserNumber = int(input("Enter a Number 1-100 : "))
 Computer_Guess = random.randint(1,100)
 ComputerPrompt = print("Is the Number "+ " = " + str(Computer_Guess))

 while True:
    UserInput = input("Type L For a Lower Guess, Type H for a Higher Guess, Type Y If the Answer is Correct : ").lower()
    if UserInput == "l":
       print(random.randint(0,UserNumber))
       UserInput1 = input("Type L For a Lower Guess, Type H for a Higher Guess, Type Y If Answer Is Correct : ").lower()

    if UserInput == "h":
     print(random.randint(UserNumber,100))
    UserInput2 = input("Type L For a Lower Guess, Type H for a Higher Guess, Type Y If Answer Is Correct : ").lower()
    if UserInput == "y":
     print("The bot has guessed it")
     break
    exit
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
    exit