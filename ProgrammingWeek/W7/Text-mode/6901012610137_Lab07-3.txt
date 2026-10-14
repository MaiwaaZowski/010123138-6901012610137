import random as r

n = 7
arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = r.randint(0,100)
    print(arr[i])

#Part A

def maxX():
    max = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (max < arr[i][j]):
                max = arr[i][j]
    return max
    
def minX():
    min = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (min > arr[i][j]):
                min = arr[i][j]
    return min
    
def avgX():
    sum, n = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
           sum += arr[i][j]
           n += 1
    avg = round(sum /(n),2)
    return avg

print(f"max:{maxX()}, min:{minX()}, avg:{avgX()}\n")

#Part B

def isFound(a,b):
    bool = False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(b == a[i][j]):
                bool = True
    return bool
    

a, b = arr, 55
print(f"{b} is found in arr is {isFound(a,b)}\n")

#Part C

def matAdd(matA, matB):
    rows, cols = len(matA), len(matB)
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matA[i][j] + matB[i][j]
    return result

def matSub(matA, matB):
    rows, cols = len(matA), len(matB)
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matA[i][j] - matB[i][j]
    return result

def matMul(matA, matB):
    rowsA, colsA, rowsB, colsB = len(matA), len(matA[0]), len(matB), len(matB[0])
    if colsA != rowsB:
        raise ValueError("Cannot multiply: Columns of A must match Rows of B.")
    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += A[i][k] * B[k][j]
    return result


A = [[r.randint(0,10) for _ in range(3) ] for _ in range(3)]
B = [[r.randint(0,10) for _ in range(3) ] for _ in range(3)]

print(f"A = {A}\nB = {B}\nA + B = {matAdd(A, B)}\nA - B = {matSub(A, B)}\nA * B = {matMul(A, B)}")

#6901012610137
#Lab07-3