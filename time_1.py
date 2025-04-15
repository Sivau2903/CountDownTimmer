import time
import webbrowser
import tkinter as tk
from threading import Thread

def countdown_timer(duration, label):
    while duration > 0:
        minutes, seconds = divmod(duration, 60)
        timer_display = "{:02d}:{:02d}".format(minutes, seconds)
        label.config(text=timer_display)
        time.sleep(1)
        duration -= 1
    label.config(text="00:00")
    time.sleep(1)
    label.config(text="Timer completed! Opening YouTube video...")
    time.sleep(2)  # Give some time to display the message before opening the video
    webbrowser.open('https://youtu.be/DrugjSZrJxc?si=X2okPIxmNQ5Z52Va')

def start_timer():
    try:
        duration = int(entry.get())
        Thread(target=countdown_timer, args=(duration, timer_label)).start()
    except ValueError:
        timer_label.config(text="Invalid input! Please enter an integer.")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position
window_width = 400
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Create a label to display the timer
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)
timer_label.place(relx=0.5, rely=0.4, anchor="center")

# Create an entry to input the duration
entry = tk.Entry(root, font=("Helvetica", 24))
entry.pack(pady=10)
entry.place(relx=0.5, rely=0.5, anchor="center")


# Create a button to start the timer
start_button = tk.Button(root, text="Start Timer", command=start_timer, font=("Helvetica", 24))
start_button.pack(pady=20)
start_button.place(relx=0.5, rely=0.6, anchor="center")

#run the code
root.mainloop()