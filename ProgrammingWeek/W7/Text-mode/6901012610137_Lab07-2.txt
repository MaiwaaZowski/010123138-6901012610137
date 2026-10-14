import random as r
day, week, i, j = 7, 4, 0, 0

# Make a blank 4*7 matrix
temp = [[0 for _ in range(day)] for _ in range(week)]

# Add a random temp in each day
for i in range(len(temp)):
    for j in range(len(temp[i])):
        temp[i][j] = round(r.uniform(25, 35), 1)

def week_avg(i):
    j, sum = 0, 0
    for j in range(len(temp[i-1])):
        sum += temp[i-1][j]
    avg_temp = sum/day
    return avg_temp

def week_max(i):
    j, max_temp = 0, temp[i-1][0]
    for j in range(len(temp[i-1])):
        if(temp[i-1][j] > max_temp):
            max_temp = temp[i-1][j]
    return max_temp

def week_min(i):
    j, min_temp = 0, temp[i-1][0]
    for j in range(len(temp[i-1])):
        if(temp[i-1][j] < min_temp):
            min_temp = temp[i-1][j]
    return min_temp
    
def overall_max():
    i, oMax = 2, week_max(1)
    for i in range(len(temp)+1):
        if(week_max(i) > oMax):
            oMax = week_max(i)
    return oMax
    
def overall_min():
    i, oMin = 2, week_min(1)
    for i in range(len(temp)+1):
        if(week_min(i) < oMin):
            oMin = week_min(i)
    return oMin
    
# Main code
print("Temperature in °C")
for i in range(len(temp)):
    print("Week", i+1, ": ", end="")
    for j in range(len(temp[i])):
        print("",temp[i][j], end="  ")
    print()

n = int(input("\nWhich week ? : "))
print(f"\nAverage Temperature in week {n} is {round(week_avg(n),1)}°C")
print(f"Maximum Temperature in week {n} is {week_max(n)}°C")
print(f"Minimum Temperature in week {n} is {week_min(n)}°C")
print(f"Overall Maximum Temperature is {overall_max()}°C")
print(f"Overall Minimum Temperature is {overall_min()}°C")
#6901012610137
#Lab07-2