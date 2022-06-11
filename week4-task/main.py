# Local Python Modules
import random

# Create a game list
# R = rock,
# P = paper
# S = Scissors

# Game Rules
# i. the scissor win the paper
# ii. the paper win the rock
# iii. the rock win the scissor

game_list = ["R", "P", "S"]

# factor to stop game
game_not_over = True

print("Hello Welcome, this is Rock Paper Scissor 's Game ")
print("Please Note: you are playing the computer")

while game_not_over:
    user_choice = input(
        "please input your choice R='rock', P='paper', S='scissors' : ").lower()
    computer_choice = random.choice(game_list).lower()
    if user_choice.upper() not in game_list:
        print("Your input is invalid, please enter a valid input")
    elif user_choice == "r" and computer_choice == 'p':
        print("GAME RESULT: Player({}): CPU({})".format(
            user_choice.upper(), computer_choice.upper()))
        print("Sorry!, you lose!")
        ask_to_play_again = input(
            "do you want to play again? yes/no: ").lower()
        if ask_to_play_again == "no":
            game_not_over = False
    elif user_choice == "r" and computer_choice == "s":
        print("GAME RESULT: Player({}): CPU({})".format(
            user_choice.upper(), computer_choice.upper()))
        print("Bravo!, you WON!")
        ask_to_play_again = input(
            "do you want to play again? yes/no: ").lower()
        if ask_to_play_again == "no":
            game_not_over = False
    elif user_choice == "p" and computer_choice == "r":
        print("GAME RESULT: Player({}): CPU({})".format(
            user_choice.upper(), computer_choice.upper()))
        print("Bravo!, you WON!")
        ask_to_play_again = input(
            "do you want to play again? yes/no: ").lower()
        if ask_to_play_again == "no":
            game_not_over = False
    elif user_choice == "p" and computer_choice == "s":
        print("GAME RESULT: Player({}): CPU({})".format(
            user_choice.upper(), computer_choice.upper()))
        print("Sorry!, you lose!")
        ask_to_play_again = input(
            "do you want to play again? yes/no: ").lower()
        if ask_to_play_again == "no":
            game_not_over = False
    elif user_choice == "s" and computer_choice == "r":
        print("GAME RESULT: Player({}): CPU({})".format(
            user_choice.upper(), computer_choice.upper()))
        print("Sorry!, you lose!")
        ask_to_play_again = input(
            "do you want to play again? yes/no: ").lower()
        if ask_to_play_again == "no":
            game_not_over = False
    elif user_choice == "s" and computer_choice == "p":
        print("GAME RESULT: Player({}): CPU({})".format(
            user_choice.upper(), computer_choice.upper()))
        print("Bravo!, you WON!")
        ask_to_play_again = input(
            "do you want to play again? yes/no: ").lower()
        if ask_to_play_again == "no":
            game_not_over = False
    else:
        print("it's a tie")
        print("GAME RESULT: Player({}): CPU({})".format(
            user_choice.upper(), computer_choice.upper()))
        ask_to_play_again = input(
            "do you want to play again? yes/no: ").lower()
        if ask_to_play_again == "no":
            game_not_over = False
