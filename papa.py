import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


def calculate_age():
    dob_str = entry.get().strip()
    mode = mode_var.get()
    today = datetime.today()

    if dob_str == "" or dob_str.lower() == "enter date":
        messagebox.showerror("Input Missing", "Please enter a valid date or year.")
        return

    try:
        if mode == "Year Only":
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
            result += f"\n🎂 {days_left} day(s) left until your next birthday!"

        result_label.config(text=result, fg="black")

    except ValueError:
        messagebox.showerror("Invalid Format", "Use:\n- 'YYYY' for year only\n- 'YYYY-MM-DD' for full date")


def reset_all():
    entry.delete(0, tk.END)
    entry.insert(0, "enter date")
    result_label.config(text="")


def clear_placeholder(event):
    if entry.get() == "enter date":
        entry.delete(0, tk.END)
        entry.config(fg="black")


def restore_placeholder(event):
    if entry.get() == "":
        entry.insert(0, "enter date")
        entry.config(fg="#bbbbbb")


# GUI setup
root = tk.Tk()
root.title("Smart Age Calculator")
root.geometry("520x330")
root.resizable(False, False)
root.configure(bg="white")

# Style
style = ttk.Style()
style.configure("TEntry", padding=6, relief="flat", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TOptionMenu", font=("Segoe UI", 11))

# Container Frame
frame = tk.Frame(root, bg="white")
frame.place(relx=0.5, rely=0.4, anchor="center")

# Title Label
tk.Label(frame, text="Enter Date of Birth:", bg="white", font=("Segoe UI", 13), fg="black").pack(pady=(0, 8))

# Entry Field with placeholder
entry_container = tk.Frame(frame, bg="#dddddd", bd=0)
entry_container.pack(pady=(0, 10))
entry = ttk.Entry(entry_container, width=32, font=("Segoe UI", 12))
entry.insert(0, "enter date")
entry.pack(ipady=6, padx=2, pady=2)
entry.config(foreground="#bbbbbb")

# Placeholder handlers
entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", restore_placeholder)

# Options Dropdown
mode_var = tk.StringVar(value="Full Date")
options = ["Year Only", "Full Date", "Next Birthday"]
dropdown = ttk.OptionMenu(frame, mode_var, options[1], *options)
dropdown.pack(pady=(0, 12))

# Button Frame
btn_frame = tk.Frame(frame, bg="white")
btn_frame.pack()

# Calculate and Reset buttons
ttk.Button(btn_frame, text="Calculate Age", command=calculate_age).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Reset", command=reset_all).grid(row=0, column=1, padx=5)

# Result Label
result_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="white", fg="black", justify="left")
result_label.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()
