import random

UserNumber = int(input("Enter a Number 1-100 : "))
Computer_Guess = random.randint(1,100)
ComputerPrompt = print("Is the Number "+ " = " + str(Computer_Guess))
UserInput = input("Type L For a Lower Guess, Type H for a Higher Guess, Type Y If the Answer is Correct : ")

while True:

    if UserInput == "L":
       print(random.randint(0,UserNumber))
       UserInput = input("Type L For a Lower Guess, Type H for a Higher Guess, Type Y If Answer Is Correct : ")

    if UserInput == "H":
     print(random.randint(UserNumber,100))
    UserInput = input("Type L For a Lower Guess, Type H for a Higher Guess, Type Y If Answer Is Correct : ")
    if UserInput == "Y":
     print("The bot has guessed it")