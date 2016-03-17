import math
import random
from random import randint

minimum_number = raw_input("What is the minimum number? ")
maximum_number = raw_input("What is the maximum number? ")


if int(minimum_number) < int(maximum_number):
    print "I'm thinking of a number from", minimum_number, "to",    maximum_number
else:
    print "That won't work!"

def main():
    
    guess = raw_input("What do you think it is?: ")
    
    actual_number = random.randint(int(minimum_number), int(maximum_number))

    subtraction_number = abs(int(actual_number) - int(guess))

    if int(guess) == actual_number:
        print "That's right!"

    if int(guess) < actual_number:
        print "The target was", actual_number
        print "Your guess was", guess
        print "That's under by", subtraction_number

    if int(guess) > actual_number:
        print "The target was", actual_number
        print "Your guess was", guess
        print "That's over by", subtraction_number

main()
