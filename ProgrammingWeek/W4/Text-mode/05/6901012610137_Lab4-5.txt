c10,c5,c1,x = 0,0,0,int(input("Enter money you want to exchange: "))
while(x > 0):
    if(x >= 10):
        x -= 10
        c10 += 1
    else:
        if(x >= 5):
            x -= 5
            c5 +=1
        else:
            if(x >= 1):
                x -= 1
                c1 += 1
print("coin10 = ", c10, "\ncoin5  = ", c5, "\ncoin1  = ", c1)
#6901012610137
#lab04-5
