__author__ = '03mcginley33'

import string
import random

personText = input("What should the monkeys type for you today? ")
length = len(personText)
monkeyText = ''
for i in range(length):
    monkeyText = ''.join(random.choice(string.ascii_letters + string.punctuation + ' ') for i in range(len(personText)))
count = 0
print(monkeyText)

while (personText != monkeyText and count < 1000000):
    newMonkey = list(monkeyText)

    for j, c in enumerate(monkeyText):
        if personText[j] != c:
            newMonkey[j] = random.choice(string.ascii_letters + string.punctuation + ' ')
            monkeyText = ''.join(newMonkey)
    count += 1
    print(monkeyText)

if count <1000000:
    print("Your text took %s  monkeys to write." % count)
else:
    print("not even one million monkeys could finish that in time.")