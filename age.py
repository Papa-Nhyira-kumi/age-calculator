import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    dob_str = entry.get().strip()
    mode = mode_var.get()
    today = datetime.today()

    if dob_str == "" or dob_str.lower() == "enter date":
        result_label.config(text="⚠️ Please enter a valid date.")
        return

    try:
        if mode == "Year Only":
            if not dob_str.isdigit():
                raise ValueError("Year must be digits only")
            dob = datetime.strptime(dob_str, "%Y")
            dob = dob.replace(month=1, day=1)
        else:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")

        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result = f"🎉 You are {age} years old."

        if mode != "Year Only":
            day_of_week = dob.strftime("%A")
            result += f"\n📅 You were born on a {day_of_week}."

            this_year_birthday = dob.replace(year=today.year)
            if this_year_birthday < today:
                next_birthday = dob.replace(year=today.year + 1)
            else:
                next_birthday = this_year_birthday
            days_left = (next_birthday - today).days
            result += f"\n🎂 {days_left} day(s) until your next birthday!"

        result_label.config(text=result, fg="black")

    except ValueError:
        result_label.config(text="⚠️ Invalid format.\nUse YYYY or YYYY-MM-DD", fg="black")


def reset_all():
    entry.delete(0, tk.END)
    entry.insert(0, "ENTER DATE")
    entry.config(fg="#bbbbbb")
    result_label.config(text="")


def clear_placeholder(event):
    if entry.get() == "ENTER DATE":
        entry.delete(0, tk.END)
        entry.config(fg="black")


def restore_placeholder(event):
    if entry.get() == "":
        entry.insert(0, "ENTER DATE")
        entry.config(fg="#bbbbbb")

# Setup root window
root = tk.Tk()
root.title("Smart Age Calculator")
root.geometry("480x300")
root.configure(bg="white")
root.resizable(False, False)

# Font
FONT = ("Segoe UI", 12)

# Center container
container = tk.Frame(root, bg="white")
container.place(relx=0.5, rely=0.4, anchor="center")

# Input Frame with rounded appearance
input_frame = tk.Frame(container, bg="#ddd", bd=0)
input_frame.pack(pady=(0, 10))
entry = tk.Entry(input_frame, width=30, font=FONT, bd=0, relief="flat", justify="center")
entry.insert(0, "ENTER DATE")
entry.config(fg="#bbbbbb")
entry.pack(ipady=8, padx=2, pady=2)

# Placeholder behavior
entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", restore_placeholder)

# Mode selection dropdown
mode_var = tk.StringVar(value="Full Date")
mode_options = ["Year Only", "Full Date", "Next Birthday"]
mode_dropdown = ttk.OptionMenu(container, mode_var, mode_options[1], *mode_options)
mode_dropdown.pack(pady=(0, 10))

# Button frame
button_frame = tk.Frame(container, bg="white")
button_frame.pack()

# Styled buttons
style = ttk.Style()
style.configure("TButton", font=FONT, padding=6)
ttk.Button(button_frame, text="Calculate", command=calculate_age).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Reset", command=reset_all).grid(row=0, column=1, padx=5)

# Result display
result_label = tk.Label(root, text="", bg="white", fg="black", font=FONT, justify="left")
result_label.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()
