import random as r
r = r.randint(1,100)
x = 0
while(x != r):
    x = int(input("Guess the number: "))
    if(x == 67):
        print("67676767676767")
    if(x == 0):
        print("Exit")
        break
    if(x > r):
        print("Too many, Try again: ")
    elif(x < r):
        print("Too less, Try again:  ")
    else:
        print("You got it !!!")
        pass

#6901012610137
#Lab04-3
