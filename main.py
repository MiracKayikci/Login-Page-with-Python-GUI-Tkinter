import tkinter as tk
from utils import update_datetime
from ui_setup import setup_ui
from login_functions import validate_login

def main():

    attempts = 3

    def open_url():
        import webbrowser
        webbrowser.open("https://github.com/MiracKayikci")

    # Main screen
    window = tk.Tk()
    window.geometry("700x480+600+140")
    window.title("Login Screen")

    # UI setup
    datetime_label, attempts_label = setup_ui(
        window,
        login_callback=lambda username, password: validate_login(username, password, window, attempts_label),
        open_url_callback=open_url,
        attempts=attempts
    )

    update_datetime(datetime_label, window)

    window.mainloop()

if __name__ == "__main__":
    main()
