def countup(n):
    if n >= 10:
        print "blastoff!"
    else:
        print n
        countup(n + 1)

def main():
    countup(int(raw_input("number: ")))
    return



def countupfrom(start, stop):
    if start >= stop:
        print "done"
    else:
        print start
        countupfrom(start + 1, stop)

def secondmain():
    countupfrom(-10, 10)
    return



def countdownfrom(start, stop):
    if start >= stop:
        print start
        countdownfrom(start - 1, stop)
    else:
        print "done"

def thirdmain():
    countdownfrom(12, 1)
    return



def adder(number, total):
    running_total = number + total
    if raw_input("number: ") == "":
        print running_total
    else:
	running_total = number + total
        print running_total
        adder(int(running_total) + int(raw_input("number: ")))

adder(int(raw_input("number: ")), 0)
