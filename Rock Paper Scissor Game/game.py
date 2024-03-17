import random

choice_list = ["rock", "paper", "scissor"]
your_score = 0
computer_score = 0

rounds = int(input("Enter the number of rounds you wanna play: "))

for round in range(1, rounds+1):
    computer_action = random.choice(choice_list)
    player_action = input("Enter your move: ").lower()
    if computer_action == player_action:
        pass
    elif (computer_action == "rock" and player_action == "scissor") or (computer_action == "paper" and player_action == "rock") or (computer_action == "scissor" and player_action == "paper"):
        computer_score += 1
    else:
        your_score += 1
    
    print(f"Computer's Move: {computer_action}")
    print(f"Scores after {round} round(s): You {your_score} - Computer {computer_score}")


if your_score > computer_score:
    print("Congratulations, YOU WON!")
elif computer_score > your_score:
    print("Out of rounds, YOU LOOSE!")
else:
    print("Whoops, IT'S A TIE")
