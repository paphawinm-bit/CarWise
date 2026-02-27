import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Radio Button Example")

# ตัวแปรไว้เก็บค่าที่เลือก
selected_value = tk.IntVar()
selected_value.set(0)  # ค่าเริ่มต้น

def show_result():
    value = selected_value.get()
    messagebox.showinfo("ผลลัพธ์", f"คุณเลือกค่า: {value}")
    # ที่นี่สามารถนำ value ไปคำนวณต่อได้เลย
    # เช่น result = value * 10

# สร้าง Radiobutton
tk.Radiobutton(root, text="ตัวเลือก 1", variable=selected_value, value=1).pack()
tk.Radiobutton(root, text="ตัวเลือก 2", variable=selected_value, value=2).pack()
tk.Radiobutton(root, text="ตัวเลือก 3", variable=selected_value, value=3).pack()

# ปุ่มกดแสดงค่าที่เลือก
tk.Button(root, text="ยืนยัน", command=show_result).pack()

root.mainloop()