#number guesser
import random as rd
print("welcome to number guesser")
chance=0
print("enter a number between 1 to 100")
num=rd.randint(1,100)
print(num)
while True:
    chance+=1
    # print("press q to quit")
    # quit()
    guess=int(input("guess the number: "))
    if guess < num:
        print("guessed nuber is less than selected number ")
    elif guess > num:
        print("guessed number is more than selected number")
    elif guess==num:
        print("guessed number is correct")
        print(f"total guesses = {chance}")
        quit()