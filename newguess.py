import math
import random
from random import randint

def whole_game():
    
    actual_number = random.randint(1, 100)

    def game():
    
        points = 0
        guess = int(raw_input("number: "))
    
        if guess == actual_number:
            print "you're right."
            points = points + 1
            print "you've got", points, "point(s)."

        if guess > actual_number:
            print "that's too high."
            game()

        if guess < actual_number:
            print "that's too low."
            game()

    game()


def main():

    print "this is a guessing game. pick an integer from 1 to 100."
    whole_game()
    whole_game()
    whole_game()

main()
