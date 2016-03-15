import random
from random import randint
minimum_number = raw_input("What is the minimum number? ")
maximum_number = raw_input("What is the maximum number? ")

if int(minimum_number) < int(maximum_number):
    print "I'm thinking of a number from", minimum_number, "to", maximum_number
    guess = raw_input("What do you think it is?: ")
else:
    print "That won't work!"

actual_number = random.randint(int(minimum_number), int(maximum_number))

if int(guess) == actual_number:
    print "That's right!"
else:
    print "Nope."
