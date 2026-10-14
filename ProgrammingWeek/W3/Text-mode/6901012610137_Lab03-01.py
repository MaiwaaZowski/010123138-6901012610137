def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Healthy Weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obesity"

    return bmi, status


# Main Program
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
if height > 100 :
    height = height/100
bmi, status = calculate_bmi(weight, height)

print(f"BMI = {bmi:.2f}")
print("Weight Status:", status)
#6901012610137
#lab03-1