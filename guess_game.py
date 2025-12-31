import random

secret_number = random.randint(1, 100)
lives = 5
while lives > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == secret_number:
        print("Congratulations! You won!")
        score = lives * 20
        print(f"Your Score: {score}")
        break
    elif guess < secret_number:
        lives -= 1
        print(f"Lives remaining: {lives}")
        print("Go Higher!")
    elif guess > secret_number:
        lives -= 1
        print(f"Lives remaining: {lives}")
        print("Go lower!")
if lives == 0:
    print("Game Over! You run out of lives.")
    print(f"The secret number was: {secret_number}")