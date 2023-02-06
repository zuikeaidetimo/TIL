import random

def roll_dice():
    return random.randint(1, 6)

def computer_turn(computer_score, user_score):
    turn_score = 0
    while turn_score < 20 and computer_score + turn_score < 100:
        dice_roll = roll_dice()
        if dice_roll == 1:
            print("Computer rolled a 1. Its turn is over.")
            turn_score = 0
            break
        else:
            turn_score += dice_roll
    return turn_score

def user_turn(user_score):
    turn_score = 0
    turn_over = False
    while not turn_over:
        dice_roll = roll_dice()
        if dice_roll == 1:
            print("You rolled a 1. Your turn is over.")
            turn_over = True
            turn_score = 0
        else:
            turn_score += dice_roll
            print(f"You rolled a {dice_roll}. Your current turn score is {turn_score}.")
            stop = input("Would you like to stop (s) or roll again (r)? ")
            if stop.lower() == "s":
                turn_over = True
    return turn_score

def play_game():
    print("Welcome to Pig the Dice Game!")
    computer_score = 0
    user_score = 0
    current_player = "user"
    while computer_score < 100 and user_score < 100:
        if current_player == "user":
            print("Your turn.")
            user_score += user_turn(user_score)
            print(f"Your score is now {user_score}.")
            current_player = "computer"
        else:
            print("Computer's turn.")
            computer_score += computer_turn(computer_score, user_score)
            print(f"Computer score is now {computer_score}.")
            current_player = "user"
    if computer_score >= 100:
        print("Computer wins!")
    else:
        print("You win!")

if __name__ == "__main__":
    play_game()