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



def adder(firstnumber, number):

    running_total = firstnumber + number

    if firstnumber == "" or number == "":
        return
    else:
        print running_total
        adder(int(raw_input("number 1: ")), int(raw_input("number 2: ")))



def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

print power(3, 0)
