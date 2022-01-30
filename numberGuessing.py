import random

number=random.randint(1,10)


for chance in range(3,0, -1):
    print (chance,  "Number of Chances left: ")
    enter=int(input("Guess a number between 1 and 10: "))

    if enter==number:
        print("You have guessed it correctly!")
        break

    elif enter != number and chance<4:
        print("Wrong guess!,try once more")
     

else:   
    print("Try again next time. All your chances are over.")
