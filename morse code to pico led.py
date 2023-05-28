from machine import Pin
import time

# Słownik kodu Morse'a
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', 9: "----."
}

# Ustawienie pinu 15 jako wyjście dla diody LED
led = Pin(15, Pin.OUT)

# Funkcja do migania diodą LED według kodu Morse'a
def morse_blink(text):
    for char in text:
        if char == " ":
            time.sleep(2)
        else:
            code = morse_code[char.upper()]
            for signal in code:
                led.value(1)
                if signal == ".":
                    time.sleep(0.2)
                elif signal == "-":
                    time.sleep(0.6)
                led.value(0)
                time.sleep(0.2)
            time.sleep(0.6)
    led.value(0) # wyłączenie diody LED po zakończeniu wypikania

# Pętla while do wprowadzania i przetwarzania kolejnych tekstów w kodzie Morse'a
while True:
    # Wprowadź tekst do przekonwertowania na kod Morse'a
    text = input("Wprowadź tekst: ")

    # Miganie diodą LED według wprowadzonego tekstu w kodzie Morse'a
    morse_blink(text)
