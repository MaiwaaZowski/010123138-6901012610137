import tkinter as tk
from tkinter import messagebox

def convert():
    text = entry_celsius.get().strip()
    try:
        celsius = float(text)
    except ValueError:
        # กรณีกรอกข้อมูลที่ไม่ใช่ตัวเลข
        messagebox.showwarning("แจ้งเตือน", "กรุณากรอกอุณหภูมิเป็นตัวเลขเท่านั้น")
        label_result.config(text="ผลลัพธ์: -")
        return

    fahrenheit = (celsius * 9 / 5) + 32
    label_result.config(text="ผลลัพธ์: " + str(round(fahrenheit, 2)) + " °F")

root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")
root.geometry("380x200")
root.resizable(False, False)

label_title = tk.Label(root, text="กรอกอุณหภูมิ (°C):", font=("Arial", 12))
label_title.pack(pady=(20, 5))

entry_celsius = tk.Entry(root, width=20, font=("Arial", 12), justify="center")
entry_celsius.pack()

btn_convert = tk.Button(root, text="Convert", width=12, command=convert)
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="ผลลัพธ์: -", font=("Arial", 14, "bold"))
label_result.pack(pady=5)

root.mainloop()

#6901012610137
#lab10-2