def calculate_area(width, length):
    return width * length


def football(area):
    return area >= 7140      # Example: 105 × 68 m


def basketball(area):
    return area >= 420       # Example: 28 × 15 m


def volleyball(area):
    return area >= 162       # Example: 18 × 9 m


# Main Program
width = float(input("Enter width (m): "))
length = float(input("Enter length (m): "))

area = calculate_area(width, length)

print(f"Area = {area:.2f} square meters")

print("Football:", football(area))
print("Basketball:", basketball(area))
print("Volleyball:", volleyball(area))
#6901012610137
#lab03-3