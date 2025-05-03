import random
import time

print(" Welcome to the Number Guessing Game!")

while True:
    number = random.randint(1, 100) 
    print("I'm thinking of a number between 1 and 100.")
    
    start_time=time.time()