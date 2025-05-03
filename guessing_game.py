import random

number = random.randint(1, 10)
print("Guess a number between 1 and 10")

guess = int(input("Your guess: "))

if guess == number:
    print("You win!")
else:
    print(f"Wrong! The number was {number}")
    
    guess = int(input("Take a guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print(" Too high!")
    else:
        print(" You win!")
