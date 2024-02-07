# this is also a version of guess the number ,but in this the computer will guess the random number
# in this we will give certain commands to the computer like "too low" or "too high"
# in this we will also use random module

import random
def computer_guess(x):
    low=0
    high=x
    feedback=''
    
    while feedback!='c':
        
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"is {guess} , 'l' for too low or 'h' for too high :")
        if feedback=='l':
            low=guess+1
        elif feedback=='h':
            high=guess-1
    print("u have guessed the correct number..")
    
print(computer_guess(10))
            
    