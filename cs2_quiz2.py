#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 1 < 2
#b) 10 == 10
#c) 3 >= 2
#
#2) What does 'return' do?
# Return prints out the final value after a function has worked.
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) It shows when a function is finished.
#b) It shows 
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 35
#problem1_b) square root of 3 - 1
#problem1_c) -1
#problem1_d) 4
#
#problem2_a) True
#problem2_b) True
#problem2_c) False
#problem2_d) False
#
#problem3_a) 1
#problem3_b) 1
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 2.5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

print """
Type in three different numbers.
The largest number will be printed.
Decimals are okay.
"""

first_number = float(raw_input("first number: "))
second_number = float(raw_input("second_number: "))
third_number = float(raw_input("third_number: "))

def main(a, b, c):

    if a == b or a == c or b == c:
        print "You didn't follow instructions!"
    else:
        if a > b and a > c:
            print a

        if b > a and b > c:
            print b

        if c > a and c > b:
            print c

main(first_number, second_number, third_number)
