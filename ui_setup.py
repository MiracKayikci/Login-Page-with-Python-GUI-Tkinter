import tkinter as tk
from tkinter import ttk

image_references = {}

def setup_ui(window, login_callback, open_url_callback, attempts):
    global image_references

    # Top Frame
    top_frame = tk.Frame(window, bg='lightgrey')
    top_frame.pack(fill='x')

    # Separator
    top_separator = ttk.Separator(window, orient='horizontal')
    top_separator.pack(fill='x', padx=10, pady=5)

    # Middle Frame
    middle_frame = tk.Frame(window, bg='white')
    middle_frame.pack(fill='both', expand=True)

    left_frame = tk.Frame(middle_frame, bg='white')
    left_frame.pack(side='left', fill='both', expand=True)

    right_frame = tk.Frame(middle_frame, bg='white')
    right_frame.pack(side='right', fill='both', expand=True)

    # Bottom Frame
    bottom_frame = tk.Frame(window, bg='lightgrey')
    bottom_frame.pack(fill='x')

    # Top Frame
    datetime_label = tk.Label(top_frame, text="", font=("Arial", 16, "bold"), bg='lightgrey', fg="#191970")
    datetime_label.pack(pady=10)

    try:
        image_references['login_image'] = tk.PhotoImage(file="images/login.png")
        image_references['user_image'] = tk.PhotoImage(file="images/adam.png")
        image_references['lock_image'] = tk.PhotoImage(file="images/kilit.png")
        image_references['large_image'] = tk.PhotoImage(file="images/buyukresim.png")
        image_references['github_image'] = tk.PhotoImage(file="images/github.png")
    except Exception as e:
        print(f"Error loading images: {e}")
        return

    # Middle Frame
    username_label = tk.Label(left_frame, text="Username: ", font=("Arial", 10, "bold"), bg='white', fg="#00008B")
    username_label.place(x=72, y=40)

    username_entry = ttk.Entry(left_frame, width=30)
    username_entry.place(x=74, y=61)

    user_image_label = tk.Label(left_frame, image=image_references['user_image'], bg='white')
    user_image_label.place(x=46, y=56)

    password_label = tk.Label(left_frame, text="Password: ", font=("Arial", 10, "bold"), bg='white', fg="#00008B")
    password_label.place(x=72, y=95)

    lock_image_label = tk.Label(left_frame, image=image_references['lock_image'], bg='white')
    lock_image_label.place(x=46, y=111)

    password_entry = ttk.Entry(left_frame, width=30, show="*")
    password_entry.place(x=74, y=117)

    # Login button
    login_button = tk.Button(left_frame, image=image_references['login_image'], command=lambda: login_callback(username_entry.get(), password_entry.get()), borderwidth=0, bg='white')
    login_button.place(x=150, y=200, anchor='center')

    github_button = tk.Button(left_frame, image=image_references['github_image'], command=open_url_callback, borderwidth=0, bg='white')
    github_button.place(relx=0.050, rely=0.8)

    # Right Frame
    other_image_label = tk.Label(right_frame, image=image_references['large_image'], bg='white')
    other_image_label.place(relx=0.5, rely=0.5, anchor='center')

    attempts_label = tk.Label(left_frame, text=f"Attempts: {attempts}", font=("Arial", 8, "bold"), bg='white',fg="#00008B")
    attempts_label.place(x=72, y=140)

    # Separator
    middle_separator = ttk.Separator(window, orient='horizontal')
    middle_separator.pack(fill='x', padx=10, pady=5)

    # Bottom Frame
    footer_label = tk.Label(bottom_frame, bg='lightgrey', fg="#191970")
    footer_label.pack(pady=10)

    return datetime_label, attempts_label
