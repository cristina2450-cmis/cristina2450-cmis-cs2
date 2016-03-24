# You are walking down the street and you come across a cafe.
# You are asked if you'd like to enter.

# If you enter you are asked what you want to order.
#   If you order juice you spill it on your shirt.
#   If you order something something else happens.
#   If you order a sandwich you happily leave on your way.
#   If you order a coffee you burn your tongue.
# Eventually you're on your way again

# If you keep going you come to the street corner
# If you turn left 
#   You come across a robber and are asked to fight or flee 
#   If you fight
#   If you flee
# If you turn right
#   Then this happens

print "You're walking down the street."

def cafe():

    print "There's a cafe! Would you like to enter?"
    cafe_answer = raw_input('Yes, No, Maybe?\n')
    
    if cafe_answer == "Yes":
        print "You're in."
    elif cafe_answer == "No":
        print "Ok, then. We'll keep walking."
    else:
        print "Let's go in anyway."

cafe()

def change():
    price_of_juice = 3
    price_of_sandwich = 5
    price_of_coffee = 2
    print "What would you like to order?\n"
    order = raw_input("Juice, Coffee or Sandwich? \n"

def street_corner():

    print "We've come to the corner. Would you like to go left or right?"
    sc_answer = raw_input('Left or Right?\n')
    
    if sc_answer == "Left":
        print "Ok"
    if sc_answer == "Right":
        print "Oh, no!"

street_corner()
