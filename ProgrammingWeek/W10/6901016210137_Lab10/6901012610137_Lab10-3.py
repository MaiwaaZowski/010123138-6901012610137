import tkinter as tk

def countChar(text, ch):
    """นับจำนวนตัวอักษร ch ที่อยู่ใน text (ไม่สนตัวพิมพ์เล็ก/ใหญ่)"""
    text = text.lower()
    ch = ch.lower()
    total = 0
    for c in text:
        if c == ch:
            total = total + 1
    return total


def countVowels(text):
    """นับจำนวนสระ a, e, i, o, u ทั้งหมดใน text"""
    vowels = "aeiou"
    total = 0
    for c in text.lower():
        for v in vowels:
            if c == v:
                total = total + 1
    return total


def isPalindrome(text):
    """ตรวจว่า text เป็น Palindrome หรือไม่ (ไม่สนตัวพิมพ์เล็ก/ใหญ่และช่องว่าง)"""
    cleaned = ""
    for c in text.lower():
        if c != " ":
            cleaned = cleaned + c

    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left = left + 1
        right = right - 1
    return True

def on_count_char():
    text = entry_text.get()
    ch = entry_char.get()
    if text == "":
        label_result.config(text="กรุณาพิมพ์ข้อความก่อน")
    elif len(ch) != 1:
        label_result.config(text="กรุณาใส่ตัวอักษรที่ต้องการนับ 1 ตัว")
    else:
        result = countChar(text, ch)
        label_result.config(
            text="ตัวอักษร '" + ch + "' พบ " + str(result) + " ตัว"
        )

def on_count_vowels():
    text = entry_text.get()
    if text == "":
        label_result.config(text="กรุณาพิมพ์ข้อความก่อน")
    else:
        result = countVowels(text)
        label_result.config(text="จำนวนสระทั้งหมด: " + str(result) + " ตัว")

def on_check_palindrome():
    text = entry_text.get()
    if text == "":
        label_result.config(text="กรุณาพิมพ์ข้อความก่อน")
    elif isPalindrome(text):
        label_result.config(text="'" + text + "' เป็น Palindrome")
    else:
        label_result.config(text="'" + text + "' ไม่เป็น Palindrome")

root = tk.Tk()
root.title("GUI Text Analyzer")
root.geometry("420x330")
root.resizable(False, False)

tk.Label(root, text="ข้อความ:", font=("Arial", 11)).pack(pady=(15, 2))
entry_text = tk.Entry(root, width=35, font=("Arial", 12))
entry_text.pack()

tk.Label(root, text="ตัวอักษรที่ต้องการนับ:", font=("Arial", 11)).pack(pady=(10, 2))
entry_char = tk.Entry(root, width=5, font=("Arial", 12), justify="center")
entry_char.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=15)

btn_char = tk.Button(frame_buttons, text="Count Character", width=15, command=on_count_char)
btn_char.grid(row=0, column=0, padx=5, pady=3)

btn_vowels = tk.Button(frame_buttons, text="Count Vowels", width=15, command=on_count_vowels)
btn_vowels.grid(row=0, column=1, padx=5, pady=3)

btn_palindrome = tk.Button(root, text="Check Palindrome", width=33, command=on_check_palindrome)
btn_palindrome.pack()

label_result = tk.Label(root, text="ผลลัพธ์จะแสดงที่นี่", font=("Arial", 12, "bold"),wraplength=380)
label_result.pack(pady=20)

root.mainloop()

#6901012610137
#lab10-3