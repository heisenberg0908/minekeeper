# this is a program to execute a simple function regarding the rock,paper and scisor game.
import random

def play():
    user=input("enter your input, 'r' for rock , 'p' for paper and 's' for scisor: ")
    computer=random.choice(['r','p','s'])
    if user==computer:
        return "it's a tie"
    elif is_win(user,computer):
        return "u won.."
    return "u loose"

def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    return "u loosa"

print(play())