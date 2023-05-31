import tkinter as tk
from PIL import Image, ImageTk
import random

def generate_noise_image():
    size = int(size_entry.get())
    
    image = Image.new("RGB", (size, size))
    pixels = image.load()
    
    for x in range(size):
        for y in range(size):
            noise_value = random.randint(0, 255)
            pixels[x, y] = (0, noise_value, 0)
    
    image.save("noise.png")
    
    # Wyświetlanie obrazu w interfejsie GUI
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

# Tworzenie okna
window = tk.Tk()
window.title("Noise Generator")

# Ustawienia rozmiaru i koloru tła
window_width = 400
window_height = 300
window.geometry(f"{window_width}x{window_height}")
window.configure(bg="green")

# Tworzenie etykiety i pola tekstowego dla rozmiaru
size_label = tk.Label(window, text="Size:")
size_label.grid(row=0, column=0, padx=10, pady=10)

size_entry = tk.Entry(window)
size_entry.grid(row=0, column=1, padx=10, pady=10)

# Tworzenie przycisku generującego obraz szumowy
generate_button = tk.Button(window, text="Generate", command=generate_noise_image)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Tworzenie etykiety i pola tekstowego do wyświetlania wygenerowanego obrazu
image_label = tk.Label(window)
image_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Uruchomienie pętli głównej
window.mainloop()
