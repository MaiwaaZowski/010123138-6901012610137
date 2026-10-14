# Calculate Body Mass Index (BMI)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m or cm): "))

# Convert cm to m if needed
if height > 3:
    height = height / 100

bmi = weight / (height ** 2)

print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 2))

#6901012610137
#Lab1 Ex2