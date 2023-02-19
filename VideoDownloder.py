from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox
import instaloader

# Define the font and colors
title_font = ("Helvetica", 24, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 14)
bg_color = "#f9f9f9"
accent_color = "#ff0000"

def download_youtube_video():
    # Get the video URL and file name from the input fields
    video_url = video_url_entry.get()
    file_name = file_name_entry.get()

    # Create a YouTube object with the video URL
    youtube = YouTube(video_url)

    # Get the highest resolution video stream
    video_stream = youtube.streams.get_highest_resolution()

    # Download the video to the specified file name
    video_stream.download(filename=file_name)

    # Show a message box to confirm the download
    messagebox.showinfo("Download Complete", f"Video saved as {file_name}")

def download_instagram_reels():
    # Get the reels URL and file name from the input fields
    reels_url = reels_url_entry.get()
    file_name = file_name_entry.get()

    # Create an Instaloader object
    loader = instaloader.Instaloader()

    # Download the reels video to the specified file name
    for post in loader.get_hashtag_posts(reels_url):
        if post.typename == "Reel":
            loader.download_post(post, target=file_name)

    # Show a message box to confirm the download
    messagebox.showinfo("Download Complete", f"Video saved as {file_name}")

# Create the main window
root = Tk()
root.title("Video Downloader")
root.geometry("600x400")
root.configure(bg=bg_color)

# Create the title label
title_label = Label(root, text="Video Downloader", font=title_font, bg=bg_color)
title_label.pack(pady=20)

# Create a notebook widget to switch between YouTube and Instagram sections
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Create the YouTube section
youtube_frame = ttk.Frame(notebook)
notebook.add(youtube_frame, text="YouTube")

video_url_label = Label(youtube_frame, text="Enter YouTube video URL:", font=label_font, bg=bg_color)
video_url_label.pack(pady=10)
video_url_entry = Entry(youtube_frame, font=label_font)
video_url_entry.pack(pady=10)

file_name_label = Label(youtube_frame, text="Enter file name:", font=label_font, bg=bg_color)
file_name_label.pack(pady=10)
file_name_entry = Entry(youtube_frame, font=label_font)
file_name_entry.pack(pady=10)

download_youtube_button = ttk.Button(youtube_frame, text="Download", command=download_youtube_video, style="Accent.TButton")
download_youtube_button.pack(pady=20)

# Create the Instagram section
instagram_frame = ttk.Frame(notebook)
notebook.add(instagram_frame, text="Instagram")

reels_url_label = Label(instagram_frame, text="Enter Instagram reels URL:", font=label_font, bg=bg_color)
reels_url_label.pack(pady=10)
reels_url_entry = Entry(instagram_frame, font=label_font)
reels_url_entry.pack(pady=10)

file_name_label = Label(instagram_frame, text="Enter file name:", font=label_font, bg=bg_color)
file_name_label.pack(pady=10)
file_name_entry = Entry(instagram_frame, font=label_font)
file_name_entry.pack(pady=10)

download_instagram_button = ttk.Button(instagram_frame, text="Download", command=download_instagram_reels, style="Accent.TButton")
download_instagram_button.pack(pady=20)

# Define the styles for the buttons
style = ttk.Style()
style.configure("Accent.TButton", font=button_font, background=accent_color, foreground="white")
style.map("Accent.TButton", background=[("active", "#ff4c4c")])

# Run the main loop
root.mainloop()
