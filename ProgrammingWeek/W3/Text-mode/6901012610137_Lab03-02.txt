def calculate_grade(score):
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score <= 79:
        return "B"
    elif 60 <= score <= 69:
        return "C"
    elif 50 <= score <= 59:
        return "D"
    elif 0 <= score <= 49:
        return "F"
    else:
        return "Invalid Score"


# Main Program
score = int(input("Enter score: "))
grade = calculate_grade(score)

print("Grade:", grade)
#6901012610137
#lab03-2