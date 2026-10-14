def print_roof():
    print("  ^  ")
    print(" ^ ^ ")

def print_ceiling():
    print("|||||")

def print_wall():
    print("|   |")

def print_floor():
    print("|||||")

def print_house(h):
    if h < 0:
        h = 0

    print_roof()

    for i in range(h):
        print_ceiling()   # เพดานของแต่ละชั้น
        print_wall()      # ผนังของชั้นนั้น

    print_floor()         # พื้นของบ้าน


# Main
h = int(input("Enter house height: "))
print_house(h)

#6901012610133
#Lab02-2