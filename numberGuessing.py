import random

number=random.randint(1,10)
print(number)



for chance in range(1,4):
    print(chance)
    enter=int(input("Guess a number between 1 and 10. You have 3 chances."))

    if enter==number:
        print("You have guessed it correctly!")

    elif enter != number and chance<4:
        print("Wrong guess!,try once more")
     

    else:   
        print("Try again next time. All your chances are over.")



