#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# It is used to assign a value to a variable.
#
#
#2 3pts) Write a technical definition for 'function'
# A function is a series of steps used to solve a problem.
#
#
#3 1pt) What does the keyword "return" do?
# It gives back whatever follows it.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: interger 1, 2
#	2: float 1.2, 2.3
#	3: boolean True, False
#	4: string, "hello", "world"
#	5: tuple, ("hello", 35), ("world", 546, True)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition is the job the function must carry out.
# A function call is giving the function an argument which it applies to
# what it has to do.
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: input
#	2: process
#	3: output
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math

def diameter_of_circles(a, b, c):
    a = raw_input("area of circle 1 >>> ")
    b = raw_input("area of circle 2 >>> ")
    c = raw_input("area of circle 3 >>> ")
    ra = math.sqrt(float(a))/math.pi
    rb = math.sqrt(float(b))/math.pi
    rc = math.sqrt(float(c))/math.pi
    da = float(ra * 2)
    db = float(rb * 2)
    dc = float(rc * 2)
    total = da + db + dc
    print da
    print db
    print dc
    print total

p = diameter_of_circles(1, 2, 3)

