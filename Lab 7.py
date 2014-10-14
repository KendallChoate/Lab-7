#25pt

x = 1

while (0 < x < 300):
    print x
    x = x + 2    
        
#50pt

myList = ["America", "Canada", "England", "Scotland", "France", "Germany", "Italy", "Austria", "Vatican", "Texas"]

index = 0

while (index < len(myList)):
    print myList [index]
    index = index + 1

#100pt

print "Guess a number between 0 and 50."

import random
rand = random.randint(0, 50)

userInput = -1

while (userInput != rand):
    userInput = int(raw_input())
    if (userInput > rand):
        print "Too high"
    elif (userInput < rand):
        print "Too low"
    elif (userInput == rand):
        print "Correct!"