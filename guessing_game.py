import random
import time

print(" Welcome to the Number Guessing Game!")

<<<<<<< HEAD
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
=======
while True:
    number = random.randint(1, 100) 
    print("I'm thinking of a number between 1 and 100.")
    
    start_time=time.time()
>>>>>>> 4f61e6bfcf4aa2fefabb88e7bdff3a481184922f
