import tkinter as tk
import speech_recognition as sr

def listen():
    top_label.pack_forget()
    label.config(text="")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pl-PL')
        if text == "tak":
            root.geometry("800x400")
            label.config(text="Otwieram link...")
            link = "https://youtu.be/xvFZjo5PgG0"
            import webbrowser
            webbrowser.open(link)
            label.config(text="")
            button_listen.pack_forget()
        elif text == "nie":
            label.config(text="Okej, to ja już sobie idę.")
            button_listen.pack_forget()
            root.after(2000, root.destroy)
        else:
            label.config(text="Nie rozumiem. Powtórz, proszę.")
    except:
        label.config(text="Nie udało się rozpoznać mowy.")

root = tk.Tk()
root.title("Dzień dobry, pani")
root.geometry("800x400")

top_label = tk.Label(root, text="Czy chce pani posłuchać muzyki. Mów tak lub nie.")
top_label.pack(pady=20)

label = tk.Label(root, text="Proszę jeszcze chciałbym powiedzieć, że aplikacja potrzebuje pakietów: tkinter, speech recognition i pyaudio.")
label.pack(pady=10)

button_listen = tk.Button(root, text="Słucham", command=listen)
button_listen.pack()

root.mainloop()
