import random
number = random.randint(1,9)
chance = 5
while chance > 0:
    chance=chance-1
    guess= int (input("Enter A Number, "))
    if guess == number:
        print("Congratulations You Won!!")
        break
    elif(guess < number):
        print("The Number You Gussed is Too Small")
    else:
        print("The Number You Gussed is Too high")
if chance == 0:
    print("You Lose number is " +number)
