import math

def add(a, b):# takes two numbers and returns their sum
	return a + b

def sub(a, b):# subtracts second number from first
	return a - b

def mul(a, b):# mulitiplies two numbers together
	return a * b

def div(a, b):# divides first number by second
	return a / b
 
def hours_from_second(seconds):# converts seconds to hours
	return seconds/3600

def circle_area(radius):# finds area of circle
	return math.pi(radius)**2

def sphere_volume(radius):# finds volume of sphere
	return 4/3 * math.pi(radius)**3

def avg_volume(a, b):# finds averge volume of two spheres
	average = ((4/3 * math.pi(a)**3)+(4/3 * math.pi(b)**3))/2
	retun float(average)

avg_volume (10, 20)
def area(a, b, c):# finds area of triangle when given 3 sides
	p =(a + b + c)/2
	return math.sqrt(p*(p-a)(p-b)(p-c))


