# exercise 37
# Symbol Review

# import: gets a module from a package, or a package
import math

# and: "if both are true" then the statement is true
# if: checks if the present statement if true
# elif: if the previous statement wasn't true, checks if the present one is
# else: checks the if the remaining option(s) are true
# print: prints
a = raw_input("> Give a small a: ")

if a.strip() != '0' and len(a) != 2:
   print "Nice choice!!"

elif len(a) ==2:
   print "Going big huh?"

else:
   print "Choose better!!"

# def: allows the creation of functions
# return: exits and returns a processed value from a Functions
# with: points to/defines an expression from where as will assign it to a variable
# as: assigns a block or item or result of operation to a variable
def f(x):
    return math.log(x)
a = float(a)
y = f(a)

with open('math_result.txt', 'w') as F:
   F.write('f(a) is: ')
   z = str(y)
   F.write(z)
   F.closed

# assert: checks if a passed valued is correct or is within the right domain
def dividingBy(x1, x2):
    assert(x1 != 0)
    return math.exp(x2 / 100) / x1

z = dividingBy(y, a)
print " Our division is %f" % z

# for: loops over an index/colection of some sort
# in: defines the domain or range from where to evaluate something
# del: deletes variables, lists or dictionaries
# break: ends whatever is being processed
arr = []
for i in range(1,100):
    a = i * dividingBy(a, z)
    arr.append(a)

    if a > 10:
        print "Results are:"
        print arr
        print "And i is: %d" % i
        del arr
        break

# class: defines how something should be structured
# pass: when a block inside a function is still empty you can use pass
class complexNum:
      def __init__(self, real, imaginary):
          self.a = real
          self.b = imaginary
      def read(self):
           return (self.a, self.b)

      def sum(self):
           pass

x = complexNum(a, z)
print "Complex number is: "
print x.read()

# is: checks if something is
# not: checks for the opposite of the value in front of it
# or: "if at lest one is true" then the statement is true
# continue: rejects current iterration, returns control to next loop
if x.sum() is not None:
    print "You finally built that function huh?"
else:
    for value in 'None':

        if value == 'o' or value == 'e':
             continue

        print "value is:", value
    print "Where are the vowels?"

# while: process an expression while the statement is true
forever = True
while forever:
    forever = eval(raw_input("> You wanna live forever. True or False?"))

    if forever == True:
        print "Great!! In that case you have time for this..."
        
    else:
        print "Okay, life is short so we better keep going and do the next exercises!"


# global: creates a global variable
# except: if an exception occurs, process a expression
# finally: process something no matter if the statement is true or not
# lambda: creates an anonymous function
# raise: raises exceptions when there is an error
# try: specifies exception handlers for statements
# yield: pauses a process or function and returns to previous or next process flow
