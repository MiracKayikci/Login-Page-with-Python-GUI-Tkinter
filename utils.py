from datetime import datetime

def update_datetime(label, window):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")
    label.config(text=f"{current_date}\n{current_time}")
    window.after(1000, lambda: update_datetime(label, window))
