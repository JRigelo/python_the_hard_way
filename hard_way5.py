# exercise 5
# more variables and printing

my_name = 'joyce'
my_age = 33 # perhaps a lie
my_height = 178 # cm
my_weight = 129 # lbs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'brown'

print "Let's talk about %s." % my_name
print "She's %d centimeters tall." % my_height
print "She's %d pounds heavy." % my_weight
print "That is actually kind of heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." %my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
