import webbrowser
import random
import time
from threading import Thread
import tkinter as tk


def move_window(window):
    # Pobierz rozmiary ekranu
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Wylosuj nowe współrzędne okna
    x = random.randint(0, screen_width - 400)
    y = random.randint(0, screen_height - 400)

    # Przesuń okno na nowe współrzędne
    window.geometry(f"400x400+{x}+{y}")

    # Ustaw czas odświeżania ruchu okna
    refresh_interval = 0.5  # 0.5 sekundy

    # Wywołaj ponownie funkcję po upływie czasu odświeżania
    window.after(int(refresh_interval * 1000), move_window, window)


# URL do przeglądania w oknach
url = "https://www.youtube.com/watch?v=dPtXaAZHuho"

# Otwórz 10 okien przeglądarki
for _ in range(10):
    webbrowser.open_new(url)

# Poczekaj na załadowanie się stron
time.sleep(5)

# Pobierz referencje do otwartych okien
windows = [w for w in webbrowser._browsers.values()]

# Stwórz główne okno tkinter (nie będzie widoczne)
root = tk.Tk()

# Przemieszczaj okna po ekranie w osobnych wątkach
for window in windows:
    # Ustaw właściwość głównego okna jako rodzica dla otwartych okien
    window.wm_transient(root)
    thread = Thread(target=move_window, args=(window,))
    thread.daemon = True
    thread.start()

# Uruchom główną pętlę aplikacji
while True:
    try:
        # Sprawdź, czy wszystkie okna są zamknięte
        if all(not window.winfo_exists() for window in windows):
            break
    except tk.TclError:
        # Przerwij pętlę w przypadku błędu Tkintera (np. zamknięcie wszystkich okien)
        break

    # Kontynuuj wykonywanie głównej pętli
    root.update()
    time.sleep(1)

print("Koniec programu.")
