#Section 1: Terminology
# 1) What is a recursive function?
# A recursive function is a function that calls itself.
# +1
#
# 2) What happens if there is no base case defined in a recursive function?
# The function will call itself until maximum depth is reached.
# +1
#
# 3) What is the first thing to consider when designing a recursive function?
# The base case.
# +1
#
# 4) How do we put data into a function call?
# With raw input.
# -
# 
# 5) How do we get data out of a function call?
# With return.
# +1
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 2 -
#a2 = 6 - 
#a3 = -1 +1

#b1 = -
#b2 = -
#b3 = -

#c1 = -
#c2 = -
#c3 = -

#d1 = -
#d2 = -
#d3 = -

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def odd_average():

    number = int(raw_input("number: "))
    total = 0

    if number/2:
        total = total
    else:
        total = number + total

#basecase
    if number == "":
        return total
#recursive case
    else:
        odd_average()

odd_average()

# +2 base case is present (MUST BE LABELED) +2
# +2 recursive case is present (MUST BE LABELED) +2
# +1 base case returns sum/ct (or equivalent) +1
# +2 recursive case filters even numbers -
# +1 recursive case increments sum and ct correctly - 
# +1 recursive case returns correct recursive call -
# +1 main function present AND called -
