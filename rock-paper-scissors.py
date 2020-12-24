import random

while True:
    print("Make your choice: ")
    choice = input()
    choice = choice.lower() #makes input lowercase
    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)

    print("You chose:", choice)

    print("The Computer chose:", computer_choice)

    if choice in choices:
        if choice == computer_choice:
            print("It is a tie!")
        if choice == 'rock':
            if computer_choice == 'paper':
                print("You lose, sorry!")
            elif computer_choice == 'scissors':
                print("You win!! Hooray!!")
        if choice == 'paper':
            if computer_choice == 'rock':
                print("You win!! Hooray!!")
            elif computer_choice == 'scissors':
                print("You lose, sorry!")
        if choice == 'scissors':
            if computer_choice == 'rock':
                print("You lose, sorry!")
            elif computer_choice == 'paper':
                print("You win!! Hooray!!")
    else:
        print("Invalid choice, try again")

    print()
