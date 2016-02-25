import math

def add(a, b):# takes two numbers and returns their sum
	return a + b

a = int(add(3, 4))
b = add(5, 6)

def sub(a, b):# subtracts second number from first
	return a - b

c = sub(9, 5)
d = sub(7, 8)

def mul(a, b):# mulitiplies two numbers together
	return a * b

e = mul(3 ,4)
f = mul(2, 6)

def div(a, b):# divides first number by second
	return a / b

g = div(9, 3)
h = div(4, 2)

def hours_from_seconds(seconds):# converts seconds to hours
	return seconds/3600

i = hours_from_seconds(7200)
j = hours_from_seconds(9000)

def circle_area(radius):# finds area of circle
	return math.pi * (radius**2)

k = circle_area(3)
l = circle_area(5)

def sphere_volume(radius):# finds volume of sphere
	return 1.333333333 * math.pi * (radius**3)

m = sphere_volume(6)
n = sphere_volume(10)

def avg_volume(a, b):# finds averge volume of two spheres
    ha = a/2
    hb = b/2
    

o = avg_volume (10, 20)
p = avg_volume (5, 7)

def area(a, b, c):# finds area of triangle when given 3 sides
	p =(a + b + c)/2
	return (p*(p-a)*(p-b)*(p-c))**0.5

q = area(12, 14, 3)
r = area(10, 5, 7)

def right_align(word):# aligns word to the right
    return (80 -len(word))*(" ") + word

s = right_align("hello")
t = right_align("blah")

def center(word):# aligns word to center
    return (40 -len(word))*(" ") + word

u = center("python")
v = center("functions")

def msg_box(word):
    return "+" + ((len(word)+4)*"-")+"+"+"\n"+"|"+(2*" ")+(word)+(2*" ")+"|"+"\n"+"+"+((len(word)+4)*"-")+"+"

print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(str(j))
print msg_box(str(k))
print msg_box(str(l))
print msg_box(str(m))
print msg_box(str(n))
print msg_box(str(o))
print msg_box(str(p))
print msg_box(str(q))
print msg_box(str(r))
print msg_box(s)
print msg_box(t)
print msg_box(u)
print msg_box(v)
