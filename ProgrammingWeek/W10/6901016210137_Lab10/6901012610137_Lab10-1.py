import tkinter as tk

count = 0

def update_label():
    label_count.config(text=str(count))

def increase():
    global count
    count = count + 1
    update_label()

def decrease():
    global count
    count = count - 1
    update_label()

def reset():
    global count
    count = 0
    update_label()

root = tk.Tk()
root.title("Counter App")
root.geometry("300x220")
root.resizable(False, False)

label_count = tk.Label(root, text="0", font=("Arial", 48, "bold"))
label_count.pack(pady=20)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

btn_increase = tk.Button(frame_buttons, text="Increase", width=10, command=increase)
btn_increase.grid(row=0, column=0, padx=5, pady=5)

btn_decrease = tk.Button(frame_buttons, text="Decrease", width=10, command=decrease)
btn_decrease.grid(row=0, column=1, padx=5, pady=5)

btn_reset = tk.Button(root, text="Reset", width=22, command=reset)
btn_reset.pack(pady=10)

root.mainloop()

#6901012610137
#lab10-1