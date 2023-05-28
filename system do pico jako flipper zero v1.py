import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Ustawienie pinu guzika
button_pin = board.GP17
button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Ustawienie pinu do odpalania funkcji
trigger_pin = board.GP16
trigger = digitalio.DigitalInOut(trigger_pin)
trigger.direction = digitalio.Direction.INPUT
trigger.pull = digitalio.Pull.UP

# Inicjalizacja obiektu Keyboard i KeyboardLayoutUS
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

counter = 1  # Inicjalizacja licznika

# Funkcja do obsługi akcji klawiatury
def keyboard_action():
    global counter  # Dodanie globalnej deklaracji zmiennej counter
    # Emulacja klawisza Windows+R
    keyboard.press(Keycode.GUI)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(1.3)

    # Wpisanie tekstu 'F:\bat files\counter.bat'
    keyboard_layout.write('F:\\bat files\\' + str(counter) + '.bat')
    time.sleep(0.3)

    # Emulacja wciśnięcia klawisza Enter
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(1.5)  # Czas oczekiwania po wpisaniu tekstu

while True:
    if not button.value:  # Sprawdzenie, czy guzik został naciśnięty
        counter += 1  # Dodanie 1 do licznika
        if counter > 5:
            counter = 1
        time.sleep(0.5)

    time.sleep(0.1)  # Czas oczekiwania, aby nie obciążać procesora

    # Wyświetlanie aktualnej wartości licznika w konsoli
    print("Counter:", counter)

    if not trigger.value:  # Sprawdzenie, czy pin trigger został naciśnięty
        # Wywołanie funkcji keyboard_action
        keyboard_action()
        time.sleep(0.5)

