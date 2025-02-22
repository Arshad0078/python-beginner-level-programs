import random

name = input("Enter your name: ")
print(f"Welcome to this word guessing game {name}!")

words = [
    "saiyan", "kamehameha", "goku", "vegeta", "capsulecorp", "frieza", "shenron",
    "namek", "dragonballs", "supersaiyan", "piccolo", "earth", "ki", "majinbuu",
    "cell", "zfighters", "gohan", "trunks", "tournament", "raditz"
]

run = True
player_score = 0
computer_score = 0
chances = 12

while run:
    computer = random.choice(words)  # Choose a random word from the list
    while chances > 0:
        player = input("Enter your guess: ")
        
        if player != computer:
            chances -= 1
            computer_score += 1
            print(f"Wrong guess! You only have {chances} chances left.")
            print(f"Scores - Player: {player_score} Computer: {computer_score}")
        else:
            chances -= 1
            player_score += 1
            print(f"Correct! The word was {computer}.")
            print(f"Scores - {name}: {player_score} Computer: {computer_score}")
            break

        if chances <= 0:
            print(f"You have no chances left. The correct word was {computer}.")
            print("Game Over!")
            break

    play_again = input("Do you want to play again (y/n)? ").lower()
    if play_again not in ("y", "yes"):
        print("Thanks for playing!")
        run = False
    else:
        chances = 12  # Reset chances for the next round
