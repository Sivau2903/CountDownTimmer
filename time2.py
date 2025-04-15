import time
import tkinter as tk
from tkinter import PhotoImage
from threading import Thread
import vlc
import random

def countdown_timer(duration, label):
    while duration > 0:
        minutes, seconds = divmod(duration, 60)
        timer_display = "{:02d}:{:02d}".format(minutes, seconds)
        label.config(text=timer_display, fg="#333", font=("Helvetica", 48))
        time.sleep(1)
        duration -= 1
    label.config(text="00:00", fg="#333", font=("Helvetica", 48))
    time.sleep(1)
    label.config(text="Timer completed! Playing video...", fg="green", font=("Helvetica", 24))
    time.sleep(2)  # Give some time to display the message before playing the video
    play_video()

def start_timer():
    try:
        duration = int(entry.get())
        if duration < 0:
            timer_label.config(text="Error: Duration cannot be negative", fg="red", font=("Helvetica", 16))
        else:
            Thread(target=countdown_timer, args=(duration, timer_label)).start()
    except ValueError:
        timer_label.config(text="Invalid input! Please enter an integer.", fg="red", font=("Helvetica", 16))

def reset_timer():
    entry.delete(0, tk.END)
    timer_label.config(text="00:00", fg="#333", font=("Helvetica", 48))

def play_video():
    videos = ['video1.mp4', 'video2.mp4','video3.mp4', 'video4.mp4']  # List of video files
    video_to_play = random.choice(videos)  # Randomly select a video
    print(f"Playing: {video_to_play}")
    
    try:
        # Create an instance of VLC player
        instance = vlc.Instance()
        player = instance.media_player_new()
        
        # Set the media
        media = instance.media_new(video_to_play)
        player.set_media(media)
        
        # Set the window handle (this is platform dependent)
        if root.winfo_viewable():
            player.set_hwnd(root.winfo_id())
        else:
            player.set_xwindow(root.winfo_id())
        
        # Play the media
        player.play()
        
        # Wait for the video to finish
        while player.get_state() != vlc.State.Ended and player.get_state() != vlc.State.Error:
            time.sleep(1)
        
        # Release the player resources
        player.release()
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to play the video")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position
window_width = 400
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Load the background image
bg_image = PhotoImage(file="background.image.png")  # Make sure to use the correct path to your image file

# Create a canvas and set the background image
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Create a label to display the timer on the canvas
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48), bg="#FFFF00", fg="#333")
timer_label.place(relx=0.5, rely=0.4, anchor="center")

# Create an entry to input the duration on the canvas
entry = tk.Entry(root, font=("Helvetica", 24), bg="#fff", fg="#333", bd=2, relief=tk.SOLID)
entry.place(relx=0.5, rely=0.5, anchor="center")

# Create a button to start the timer on the canvas
start_button = tk.Button(root, text="Start Timer", command=start_timer, font=("Helvetica", 24), bg="#FF0000", fg="#fff", bd=0, relief=tk.FLAT, padx=20, pady=10)
start_button.place(relx=0.5, rely=0.6, anchor="center")

# Create a button to reset the timer on the canvas
reset_button = tk.Button(root, text="Reset", command=reset_timer, font=("Helvetica", 24), bg="#FFA500", fg="#fff", bd=0, relief=tk.FLAT, padx=20, pady=10)
reset_button.place(relx=0.5, rely=0.7, anchor="center")

# Run the Tkinter main loop
root.mainloop()
