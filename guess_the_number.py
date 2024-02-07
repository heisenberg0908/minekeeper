# this is a simple version of guess the number game , in which we are guessing the number
# in this we are using random module to generate random numbers
import random
def guess(x):
    random_number=random.randint(1,x)
    guess_number=0
    while guess_number!=random_number:
        guess_number=int(input(f"enter a number between 1 and {x}: "))
        if guess_number==random_number:
            print("u have guessed the correct number..")
        elif guess_number>random_number:
            print("ur guessed number is greater than the random number..")
        elif guess_number<random_number:
            print("ur guessed number is smaller than the random number:")
    print(f"u have guessed the correct number which is {random_number}... ")
print(guess(10))