import random
print("****** WELCOME TO ROCK PAPER SCISSOR GAME ******")
print("Are you READY? lets start the game......")
user_input = int(input('select "0" for ROCK, "1" for PAPER, and "2" for SCISSOR'))
computer_value = random.randint(0,2)
print(f'computer selects {computer_value}')

#here is conditions for the game
if user_input == 0:
    if computer_value == 1:
        print("You LOST the game, Computer WINS....")
    elif computer_value == 0:
        print("It's a draw")
    elif computer_value == 2:
        print("hurrayyyy, you WIN the game")
elif user_input == 1:
    if computer_value == 1:
        print("It's a draw")
    elif computer_value == 0:
        print("hurrayyyy, you WIN the game")
    elif computer_value == 2:
        print("You LOST the game, Computer WINS....")
elif user_input == 2:
    if computer_value == 1:
        print("hurrayyyy, you WIN the game")
    elif computer_value == 0:
        print("You LOST the game, Computer WINS....")
    elif computer_value == 2:
        print("It's a draw")
else:
    print("Entered wrong input, please try again :) ")