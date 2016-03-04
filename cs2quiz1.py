#Part 1: Terminology (15 points) (teminology - 12/15) (programming - 8/25)
#1 1pt) What is the symbol "=" used for? - (1pt)
# It is used to assign a value to a variable.
#
#
#2 3pts) Write a technical definition for 'function' - (2pts)
# A function is a series of steps used to solve a problem.
#
#
#3 1pt) What does the keyword "return" do? - (1pt)
# It gives back whatever follows it.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two - (5pts)
#   examples of each below
#	1: interger 1, 2
#	2: float 1.2, 2.3
#	3: boolean True, False
#	4: string, "hello", "world"
#	5: tuple, ("hello", 35), ("world", 546, True)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"? - (2pts)
# A function definition is the job the function must carry out.
# A function call is giving the function an argument which it applies to
# what it has to do.
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them - (1pt)
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

#1 pt for header line - (1pt)
#3 pt for correct formula - (1pts)
#1 pt for return value - (0pts return was not used)
#1 pt for parameter name - (0pts parameters name are not descriptive)
#1 pt for function name - (1pt)
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
#1pt for header line - (0pts)
#1pt for parameter names - (1pt)
#1pt for return value - (0pts)
#1pt for correct output format - (0pts)
#3pt for correct use of format function - (0pts)

#1pt header line - (0pts)
#1pt getting input - (1pt)
#1pt converting input - (1pt)
#1pt for calling output function - (0pts)
#2pt for correct diameter formula - (0pts)
#1pt for variable names - (1pt)

#1pt for calling main - (0pts)
#1pt script runs - (1pt) 
#1pt explanatory comments - (0pts)
#1pt code format - (0pts)
# Although the program runs, the execution was wrong. The formula was correct but it wasn't well organised as it was one long function instead of three shorter easier to read functions. The program also returned the four values asked for but they were incorrect.
p = diameter_of_circles(1, 2, 3)

