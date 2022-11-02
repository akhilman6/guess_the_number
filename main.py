from art import logo
import random


def easy(rndm):
    lives = 10
    game_over = False
    print(f"You have {lives} attempts left.")
    while not game_over:
        guess = int(input("Guess a number: "))
        if guess == rndm:
            print("You Win!!")
            game_over = True
        else:
            if guess < rndm:
                lives -= 1
                print("Too Low.")
                print(f"You have {lives} attempts left.")
            else:
                lives -= 1
                print("Too High.")
                print(f"You have {lives} attempts left.")
        if lives == 0:
            game_over = True
            print(f"You lose. The number is {rndm}.")


def hard(rndm):
    lives = 5
    game_over = False
    print(f"You have {lives} attempts left.")
    while not game_over:
        guess = int(input("Guess a number: "))
        if guess == rndm:
            print("You Win!!")
            game_over = True
        else:
            if guess < rndm:
                lives -= 1
                print("Too Low.")
                print(f"You have {lives} attempts left.")
            else:
                lives -= 1
                print("Too High.")
                print(f"You have {lives} attempts left.")
        if lives == 0:
            game_over = True
            print(f"You lose. The number is {rndm}.")


print(logo)
number = []
for i in range(1, 101):
    number.append(i)

rndm_number = random.choice(number)

print("I have selected a number from 1 to 100.")
mode = input("Do you want 'easy' or 'hard' mode?: ")

if mode == "easy":
    easy(rndm_number)
else:
    hard(rndm_number)
