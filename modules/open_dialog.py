import tkinter as tk
from tkinter import filedialog
from PIL import Image

def open_image_dialog():
    # Create a Tkinter root window (it will not be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file dialog
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;")])

    # Close the Tkinter root window
    root.destroy()

    # If a file was selected, open and return the image
    return file_path

def open_mp4_dialog():
    # Create a Tkinter root window (it will not be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file dialog
    file_path = filedialog.askopenfilename(
        filetypes=[("MP4 files", "*.mp4")]
    )

    # Close the Tkinter root window
    root.destroy()

    # Return the file path (or None if no file was selected)
    return file_path