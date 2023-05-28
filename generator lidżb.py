import time
start_time = time.time()
with open("plik.txt", "w") as file:
    file.write("1" + "0"*10000000000)
end_time = time.time()
print("Czas generowania pliku:", end_time - start_time, "sekund.")
print("Generowanie pliku zakończone.")