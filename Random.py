import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
print("You guessed it!" if guess == number else f"Wrong! It was {number}.")
