print("All perfect numbers between 1-50 are")
num = 1

while num <= 50:
    total = 0
    i = 1

    while i < num:
        if num % i == 0:
            total += i
        i += 1

    if total == num:
        print(num)

    num += 1

#691012610137
#lab04-2