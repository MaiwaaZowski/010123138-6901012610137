def most_balls(football, basketball, volleyball):
    if football >= basketball and football >= volleyball:
        return "Football"
    elif basketball >= football and basketball >= volleyball:
        return "Basketball"
    else:
        return "Volleyball"


# Main Program
football = int(input("Enter number of footballs: "))
basketball = int(input("Enter number of basketballs: "))
volleyball = int(input("Enter number of volleyballs: "))

result = most_balls(football, basketball, volleyball)

print("Most balls:", result)
#6901012610137
#lab03-4