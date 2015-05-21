__author__ = '03mcginley33'

# not sure why I have to import string really...
# AJM - you have to import string to get access to string.xxx that you use below.
import string
import random

# Its better practice to always use variables, rather than "Magic Numbers", especially
#  if you use it multiple times.
MAX_TRIES = 1000000

#this is the text to match
personText = input("What should the monkeys type for you today? ")
#this generates an empty list of the same length as the inputted text, because strings are immutable
#AJM - it is not necessary to initalize the size of the array, and what you were doing before actually is the same as I have here. Lists grow as necessary, you just cant access more than the current length.
monkeyText = []

#generates a random character of upper, lower, punctuation, and spaces
def randomChar():
    return random.choice(string.ascii_letters + string.punctuation + ' ')

#populates the empty list with random characters
# Almost any time you see "range(len(x))", something is wrong. Just do for x in y: instead.
# Additionally, using '_' as the variable name here is a hint to other programmers you dont care about each item, you are just iterating that many times.
for _ in personText:
    monkeyText.append(randomChar())

print(monkeyText)
#initialize a count to see how many iterations it takes
count = 0

#now to start randomizing the individual positions until they match, upper bound at a million
while personText != monkeyText and count < MAX_TRIES:
    #turn it into a list so we can work with it
    newMonkey = list(monkeyText)

    #step through each character if it doesn't match
    for j, c in enumerate(monkeyText):
        if personText[j] != c:
            newMonkey[j] = randomChar()
            monkeyText = ''.join(newMonkey)

    #increment counter to tell how many tries it took
    count += 1
    #print out iteration until it matches original text
    print(monkeyText)


#print results
if count < MAX_TRIES:
    print("Your text took %s monkeys to write." % count)
else:
    print("not even one million monkeys could finish that in time.")
