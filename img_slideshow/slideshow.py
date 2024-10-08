from itertools import cycle
import tkinter as tk
from PIL import Image, ImageTk
import time

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of image paths
image_paths = [
    r"C:\Users\keyur\Downloads\adi\1.jpg",
    r"C:\Users\keyur\Downloads\adi\2.jpg",
    r"C:\Users\keyur\Downloads\adi\3.jpg",
    r"C:\Users\keyur\Downloads\adi\4.jpg",
]

# Resize images to 1080x1080
image_size = (1280, 800)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)

def update_image():
    image = next(slideshow)
    label.config(image=image)
    label.image = image  # keep a reference to the image to prevent garbage collection
    root.after(3000, update_image)  # schedule the next image update after 3 seconds

def start_slideshow():
    update_image()  # start the slideshow

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()
