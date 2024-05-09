import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password match
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Incorrect username or password")


# Create main window
root = tk.Tk()
root.title("Login")

# Username Label and Entry
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, sticky="e")

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

# Password Label and Entry
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, sticky="e")

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

# Run the application
root.mainloop()
