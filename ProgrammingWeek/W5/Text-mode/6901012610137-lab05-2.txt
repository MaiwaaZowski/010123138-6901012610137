def find_variance(arr):
    # หาผลรวมของค่าทั้งหมด (ไม่ใช้ sum())
    total = 0
    i = 0
    while i < len(arr):
        total = total + arr[i]
        i = i + 1
    n = len(arr)
    mean = total / n

    # หาผลรวมของ (ค่าแต่ละตัว - ค่าเฉลี่ย)^2
    sum_squared_diff = 0
    i = 0
    while i < len(arr):
        diff = arr[i] - mean
        sum_squared_diff = sum_squared_diff + (diff * diff)
        i = i + 1

    # ความแปรปรวน = ผลรวมของ (diff^2) หารด้วยจำนวนข้อมูล
    variance = sum_squared_diff / n
    return variance


# --- ทดสอบ ---
data = [2, 4, 4, 4, 5, 5, 7, 9]
print(find_variance(data))   # 4.0

#6901012610137
#Lab05-2