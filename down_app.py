
import tkinter as tk
from tkinter import messagebox
import pytube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

def download_video():
    url = url_entry.get()
    save_path = save_directory_entry.get()
    
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return
    
    if not save_path:
        messagebox.showerror("Error", "Please enter a valid save directory.")
        return
    
    try:
        # Create a YouTube object for the given URL
        youtube = pytube.YouTube(url)
        
        # Select the stream (video quality) you want to download
        stream = youtube.streams.get_highest_resolution()
        
        # Download the video to the specified path
        stream.download(output_path=save_path)
        
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and pack the save directory label and entry
save_directory_label = tk.Label(root, text="Save Directory:")
save_directory_label.pack()

save_directory_entry = tk.Entry(root, width=100,fg='grey')
save_directory_entry.pack()

# Set default save path
save_directory_entry.insert(0, "C:/code/yt_down/out")

# Create and pack the URL label and entry
url_label = tk.Label(root, text="URL:")
url_label.pack()

url_entry = tk.Entry(root, width=100,fg='grey')
url_entry.pack()

# Set default URL
url_entry.insert(0, "https://www.youtube.com/watch?v=4QlhNOVaY-E&list=PLE-R0uydm0uMPY7cu-kuEkcPHAM0M9Cby&index=31")


# Create and pack the download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Start the GUI event loop
root.mainloop()
