import tkinter as tk
from PIL import Image

def generate_image():
    width = int(width_entry.get())
    height = int(height_entry.get())

    image = Image.new("RGB", (width, height), "black")
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            r = int(x / width * 255)
            g = int(y / height * 255)
            b = 0
            pixels[x, y] = (r, g, b)

    image.save(name_entry.get() + ".png")

# Tworzenie okna
window = tk.Tk()
window.title("black gole generator")
window.geometry("350x200")
window.configure(bg="#014189")

# Tworzenie etykiet
width_label = tk.Label(window, text="Width:")
width_label.grid(row=0, column=0, padx=10, pady=10)

height_label = tk.Label(window, text="Height:")
height_label.grid(row=1, column=0, padx=10, pady=10)

name_label = tk.Label(window, text="Name:")
name_label.grid(row=2, column=0, padx=10, pady=10)

# Tworzenie pól tekstowych
width_entry = tk.Entry(window)
width_entry.grid(row=0, column=1, padx=10, pady=10)

height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

name_entry = tk.Entry(window)
name_entry.grid(row=2, column=1, padx=10, pady=10)

# Tworzenie przycisku
generate_button = tk.Button(window, text="Generate", command=generate_image)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Uruchomienie pętli głównej
window.mainloop()
