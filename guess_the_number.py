import random

randNum = random.randint(1, 100)
print("Computer has generated a number. Guess the number (1-100)!")
userNum = int(input("Guess the number: "))

if (randNum == userNum):
    print("You guessed the correct number!")
else:
    while(randNum != userNum):
        if (randNum > userNum):
            userNum = int(input("Wrong guess! guess a larger number."))
        else:
            userNum = int(input("Wrong guess! guess a smaller number."))
    print("You guessed the correct number!")