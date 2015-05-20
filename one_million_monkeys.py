__author__ = '03mcginley33'

# not sure why I have to import string really...
import string
import random

#this is the text to match
personText = input("What should the monkeys type for you today? ")
#this generates an empty list of the same length as the inputted text, because strings are immutable
monkeyText = []*len(personText)

#generates a random character of upper, lower, punctuation, and spaces
def randomChar():
    return random.choice(string.ascii_letters + string.punctuation + ' ')

#populates the empty list with random characters
for i in range(len(personText)):
    monkeyText.append(randomChar())

print(monkeyText)
#initialize a count to see how many iterations it takes
count = 0

#now to start randomizing the individual positions until they match, upper bound at a million
while personText != monkeyText and count < 1000000:
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
if count < 1000000:
    print("Your text took %s  monkeys to write." % count)
else:
    print("not even one million monkeys could finish that in time.")