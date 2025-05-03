import random
import time

print("Welcome to the Number Guessing Game!")

while True:
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    start_time = time.time()

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You win!")
            break  

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    print(f"You took {time_taken} seconds.")

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
