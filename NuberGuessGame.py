import random

number = random.randint(1, 20)
guesses = 0

print("Guess the number between 1 and 20!")

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {guesses} tries.")
        break