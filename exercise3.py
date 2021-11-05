import random
number= random.randint(1,126)
guess=0
while guess!=number:
    guess = int(input("Guess the number: "))
    if guess<number:
        print("increase your number")
    elif guess>number:
        print("decrease your number")
if guess==number:
    print("Your guess is correct")



