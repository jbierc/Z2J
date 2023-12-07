import random

points = int(input("Enter a number of points: "))

symbols = ["rock", "paper", "scissors"]
user_points = 0
comp_points = 0

while user_points < points and comp_points < points:
    user_choice = input("Enter 'rock', 'paper' or 'scissors': ").lower()
    comp_choice = symbols[random.randint(0,2)]
    if user_choice == "rock" and comp_choice == "paper":
        comp_points += 1
    elif user_choice == "paper" and comp_choice == "scissors":
        comp_points += 1
    elif user_choice == "scissors" and comp_choice == "rock":
        comp_points += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        user_points += 1
    elif user_choice == "paper" and comp_choice == "rock":
        user_points += 1
    elif user_choice == "scissors" and comp_choice == "paper":
        user_points += 1
    elif user_choice == comp_choice:
        print("Draw!")
    print(f"You {user_points}:{comp_points} Computer")

if user_points > comp_points:
    print("You won the game!")
else:
    print("Computer won the game... :(")
