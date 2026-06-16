import tkinter as tk
from tkinter import messagebox
import time

# تأخير قبل ظهور الرسالة (بالثواني)
time.sleep(5)  # 120 ثانية = دقيقتين

# إعداد نافذة الرسالة
root = tk.Tk()
root.withdraw()  # يخفي نافذة tkinter الرئيسية
messagebox.showerror("تحذير", "تم اختراق شبكة الإنترنت!")
root.destroy()