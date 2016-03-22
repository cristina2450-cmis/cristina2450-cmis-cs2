import math

def average_area_of_circles(radius_a, radius_b):
	area_a = math.pi*float(radius_a)**2
	area_b = math.pi*float(radius_b)**2
	return (area_a + area_b)/2

def output(name, radius_a, radius_b, average_areas):
	out = """
Do you know how to find the average area of 2 circles, {}?
Did you know the average areas of circles with the radii of 
{} and {} is {}.
""".format(name, radius_a, radius_b, average_areas)
	return out

def main():

	#input
	name = raw_input("What's your name? >>> ")
	radius_a = raw_input("Write a number for the radius >>> ")
	radius_b = raw_input("Write a number for the radius >>> ")

	#processing
	average_areas = average_area_of_circles(int(radius_a), int(radius_b))

	#output
	out = output(name, radius_a, radius_b, average_areas)
	print out

main()
