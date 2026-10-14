a,b = int(input("Prime number between: ")), int(input("To: "))
num = a
while num <= b:
    if num >= 2:
        i = 2
        is_prime = True

        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            print(num)

    num += 1
#6901012610137
#lab4-6
