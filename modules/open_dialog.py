import tkinter as tk
from tkinter import filedialog
from PIL import Image

def open_image_dialog():
    # Create a Tkinter root window (it will not be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file dialog
    print("Select a template image")
    file_path = filedialog.askopenfilename(
        title="Select a template image", 
        filetypes=[("Image files", "*.png;")])

    # Close the Tkinter root window
    root.destroy()

    # If a file was selected, open and return the image
    return file_path

def open_mp4_dialog():
    # Create a Tkinter root window (it will not be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file dialog
    print("Select a Brawlhalla 1v1 Ranked VOD")
    file_path = filedialog.askopenfilename(
        title="Select a Brawlhalla 1v1 Ranked VOD", 
        filetypes=[("MP4 files", "*.mp4")]
    )

    # Close the Tkinter root window
    root.destroy()

    # Return the file path (or None if no file was selected)
    return file_path