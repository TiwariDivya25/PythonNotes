import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print("you chose " + player + ", computer chose " + computer)
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "rock smasher scissors! you win!"
        else:
            return "paper covers rock! you lose."
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! you win!"
        else:
            return "scissors cut paper! you lose."
    elif player == "scissors":
        if computer == "paper":
            return "scissors cut paper! you win!"
        else:
            return "rock smasher scissors! you lose."

play = get_choices()
print (play)
result = check_win(play["player"], play["computer"])
print(result)