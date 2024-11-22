from tkinter import messagebox

# Usernames
user_info = {
    "admin": "admin",
     "try" : "try"
}

# Login check
def validate_login(username, password, window, attempts_label):
    global attempts
    if username in user_info and password == user_info[username]:
        window.destroy()
    else:
        if username == "":
            messagebox.showinfo("Error", "Enter username")
        elif password == "":
            messagebox.showinfo("Error", "Enter password.")
        else:
            attempts -= 1
            attempts_label.config(text=f"Attempts: {attempts}")
            if attempts == 0:
                messagebox.showinfo("Access Denied", "You have entered incorrect credentials 3 times. The program will close.")
                window.destroy()
            else:
                messagebox.showinfo("Try Again", f"Incorrect username or password. Remaining attempts: {attempts}")
