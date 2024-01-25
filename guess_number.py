print("welcome to the number guessing game!")
import random
easy_turns=10
difficult_turns=5
def check_answer(guess,number,turns):
    if guess<number:
        print("too low")
        return turns-1
    elif guess>number:
        print("too high")
        return turns-1
    else:
        print("you win")

def set_difficulty():
    level = input("choose difficulty easy or hard")
    if level=="easy":
        return easy_turns
    else:
        return difficult_turns

def game():
    number =random.randint(1,100)
    print(number)
    turns=set_difficulty()

    guess=0
    while guess!=0:
        print(f"you have {turns} attempts ")
        guess = int(input("enter a number you are thinking"))
        turns=check_answer(guess,number,turns)
        if turns==0:
            print("no more chances")
        elif guess!=number:
            print("guess again")

game()
