import string
import random 
import tkinter as tk
from tkinter import messagebox

upc = string.ascii_uppercase
lwc = string.ascii_lowercase
num = string.digits
sym = string.punctuation

def password(char, user_choices):
    pwd = ""
    if 1 in user_choices:
        pwd += upc
    if 2 in user_choices:
        pwd += lwc
    if 3 in user_choices:
        pwd += num
    if 4 in user_choices:
        pwd += sym
    if not pwd:
        return "Invalid selection"

    pwd_gen = "".join(random.choices(pwd, k=char))

    def isStrong():
        strength = {1: "Very Weak", 2: "Weak", 3: "Good", 4: "Strong", 5: "Very Strong"}
        if 1 <= char <= 4:
            strong = 1
        elif 5 <= char <= 7:
            strong = 2
        elif 8 <= char <= 9:
            strong = 3
        elif 10 <= char <= 11:
            strong = 4
        else:
            strong = 5
        if len(user_choices) == 1 and 5 <= char <= 25:
            return strength[strong - 1]
        else:
            return strength[strong]

    return f"Your {isStrong()} password is",pwd_gen

def generate_password():
    try:
        char = int(textbox.get('1.0', tk.END).strip())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")
        return

    user_choices = []
    if chk_upc_var.get():
        user_choices.append(1)
    if chk_lwc_var.get():
        user_choices.append(2)
    if chk_num_var.get():
        user_choices.append(3)
    if chk_sym_var.get():
        user_choices.append(4)

    strength_result, pwd_result = password(char, user_choices)
    if pwd_result:
        password_entry.delete(0, tk.END)
        result_label.config(text = strength_result)
        password_entry.insert(0, pwd_result)
        copy_label.config(text = "You can now copy & paste it 🥰")

    

    

# GUI setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Generate a strong password for your account!", font=('Arial', 24, 'bold')).pack(padx=20, pady=20)
tk.Label(root, text="Enter number of characters(1-50):", font=('Arial', 16)).pack(padx=10, pady=10)

textbox = tk.Text(root, height=1, width=5, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

# Checkbox variables
chk_upc_var = tk.IntVar()
chk_lwc_var = tk.IntVar()
chk_num_var = tk.IntVar()
chk_sym_var = tk.IntVar()

chkFrame = tk.Frame(root)
chkFrame.columnconfigure((0, 1, 2, 3), weight=1)

tk.Checkbutton(chkFrame, text="Uppercase", font=('Arial', 16), variable=chk_upc_var).grid(row=0, column=0, sticky=tk.W+tk.E)
tk.Checkbutton(chkFrame, text="Lowercase", font=('Arial', 16), variable=chk_lwc_var).grid(row=0, column=1, sticky=tk.W+tk.E)
tk.Checkbutton(chkFrame, text="Numbers", font=('Arial', 16), variable=chk_num_var).grid(row=0, column=2, sticky=tk.W+tk.E)
tk.Checkbutton(chkFrame, text="Symbols", font=('Arial', 16), variable=chk_sym_var).grid(row=0, column=3, sticky=tk.W+tk.E)

chkFrame.pack(fill='x')

tk.Button(root, text="Generate", font=('Arial', 14, 'bold'), command=generate_password).pack(padx=10, pady=10)

result_label = tk.Label(root, text="", font=('Arial', 16, 'bold'))
result_label.pack(padx=10, pady=20)

password_entry = tk.Entry(root, font=('Consolas', 16), width=60, justify='center')
password_entry.pack(pady=10)

copy_label = tk.Label(root, text="", font=('Arial', 14))
copy_label.pack(padx=10, pady=20)

root.mainloop()
