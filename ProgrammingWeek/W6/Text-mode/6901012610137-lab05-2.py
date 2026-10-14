# 1. เทียบเท่า equals() - เปรียบเทียบว่า string สองตัวเหมือนกันหรือไม่
def my_equals(s1, s2):
    if len(s1) != len(s2):
        return False
    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
            return False
        i = i + 1
    return True


# 2. เทียบเท่า endswith() - ตรวจสอบว่า string ลงท้ายด้วยคำที่กำหนดหรือไม่
def my_endswith(s, suffix):
    if len(suffix) > len(s):
        return False
    start = len(s) - len(suffix)
    i = 0
    while i < len(suffix):
        if s[start + i] != suffix[i]:
            return False
        i = i + 1
    return True


# 3. เทียบเท่า isalpha() - ตรวจสอบว่าทุกตัวอักษรเป็นตัวอักษร (a-z, A-Z) หรือไม่
def my_isalpha(s):
    if len(s) == 0:
        return False
    i = 0
    while i < len(s):
        ch = s[i]
        if not ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
            return False
        i = i + 1
    return True


# --- ทดสอบ ---
print(my_equals("Thailand", "Thailand"))   # True
print(my_equals("Thailand", "thailand"))   # False (ตัวพิมพ์เล็ก/ใหญ่ต่างกัน)
print(my_equals("Thai", "Thailand"))       # False (ความยาวต่างกัน)

print(my_endswith("Thailand", "land"))     # True
print(my_endswith("Thailand", "Thai"))     # False
print(my_endswith("Thailand", "ThailandX"))# False (suffix ยาวกว่า string)

print(my_isalpha("Thailand"))              # True
print(my_isalpha("Thailand123"))           # False
print(my_isalpha(""))                      # False
#6901012610137
#Lab06-2