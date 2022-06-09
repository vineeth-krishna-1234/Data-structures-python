import random
starting_range=int(input("Starting range:"))
ending_range=int(input("\nEnding range:"))
guess_count=0
rand_number=random.randint(starting_range,ending_range)
while True:
    guess=int(input("your guess:"))
    if guess>rand_number:
        print("Try Again! You guessed too high")
        guess_count+=1
    elif guess<rand_number:
        print("Try Again! You guessed too low")
        guess_count+=1
    else:
        print(f"voila!!! u took {guess_count} guesses")
        break