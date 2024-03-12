import os
from tkinter import Tk, filedialog, Label, Button
from PIL import Image

class ImageCompressor:
    def __init__(self, master):
        self.master = master
        master.title("Image Compressor")

        self.label = Label(master, text="Select an image to compress:")
        self.label.pack()

        self.select_button = Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.rgb;*.rgba")])
        if file_path:
            self.compress_image(file_path)

    def compress_image(self, file_path):
        try:
            original_size = os.path.getsize(file_path) / 1024  # in KB
            original_extension = file_path.split('.')[-1].lower()

            img = Image.open(file_path)
            img.save("compressed_image." + original_extension, quality=85)  # You can adjust the quality as needed

            compressed_size = os.path.getsize("compressed_image." + original_extension) / 1024

            os.remove(file_path)  # Remove the original file

            self.show_message(f"Compression successful!\nOriginal Size: {original_size:.2f} KB\nCompressed Size: {compressed_size:.2f} KB")
        except Exception as e:
            self.show_message(f"Error: {e}")

    def show_message(self, message):
        message_label = Label(self.master, text=message)
        message_label.pack()

if __name__ == "__main__":
    root = Tk()
    app = ImageCompressor(root)
    root.mainloop()
