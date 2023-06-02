import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading

selected_dlugosc = ""
window = None


def wybierz(dlugosc):
    global selected_dlugosc
    selected_dlugosc = dlugosc


def wyswietl_powiadomienie():
    global selected_dlugosc
    messagebox.showinfo("Wybrana długość", f"Twój piekielnik ma teraz {selected_dlugosc}")
    window.after(1500, window.destroy)  # Zamknięcie okna po 1,5 sekundy


def odtworz_video():
    webbrowser.open("https://www.youtube.com/watch?v=X41PZTvxFN4")


def opoznione_odtworzenie_video():
    threading.Timer(2, odtworz_video).start()


# Tworzenie okna
window = tk.Tk()
window.title("Piekielnik")
window.geometry("600x400")
window.configure(bg="#007231")

# Tworzenie etykiety z napisem
label = tk.Label(window, text="Wybierz długość swojego piekielnika", font=("Arial", 20), bg="#007231", fg="white")
label.pack(pady=20)

# Tworzenie przycisków
button_5cm = tk.Button(window, text="5cm", width=10, command=lambda: wybierz("5cm"))
button_5cm.pack()

button_8cm = tk.Button(window, text="8cm", width=10, command=lambda: wybierz("8cm"))
button_8cm.pack()

button_69cm = tk.Button(window, text="69cm", width=10, command=lambda: wybierz("69cm"))
button_69cm.pack()

button_3m = tk.Button(window, text="3m [Ostrożnie!!!]", width=15, fg="red", command=lambda: wybierz("3m [Ostrożnie!!!]"))
button_3m.pack()

# Przycisk "Wybierz"
button_wybierz = tk.Button(window, text="Wybierz", width=10, command=wyswietl_powiadomienie)
button_wybierz.pack(pady=20)

# Przycisk "Odtwarzaj video"
button_odtworz = tk.Button(window, text="Odtwarzaj video", width=15, command=odtworz_video)
button_odtworz.pack(pady=10)

# Wywołanie opóźnionego odtwarzania video
opoznione_odtworzenie_video()

# Wyświetlanie okna
window.mainloop()
