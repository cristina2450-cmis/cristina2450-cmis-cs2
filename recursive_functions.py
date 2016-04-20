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

secondmain()
