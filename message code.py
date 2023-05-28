import subprocess
import socket
from tqdm import tqdm

def send_message_ip(ip_address, message):
    try:
        subprocess.run(['msg', '/SERVER:' + ip_address, '*', message], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def send_message_android(ip_address, message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address, 5555))
        sock.sendall(message.encode())
        sock.close()
        return True
    except ConnectionRefusedError:
        return False

def send_messages_in_lan():
    lan_network = '192.168.0.'  # Ustaw swój zakres sieci LAN

    message = input("Podaj treść wiadomości: ")

    success_count = 0
    total_count = 0

    with tqdm(total=254) as pbar:
        for i in range(1, 255):
            ip_address = lan_network + str(i)

            if subprocess.call(['ping', '-n', '1', '-w', '100', ip_address], stdout=subprocess.PIPE) == 0:
                # Sprawdź, czy komputer jest dostępny w sieci LAN
                if ip_address.endswith('1'):
                    if send_message_android(ip_address, message):
                        success_count += 1
                else:
                    if send_message_ip(ip_address, message):
                        success_count += 1

            total_count += 1
            pbar.update(1)

    print(f"Wysłano wiadomość do {success_count} z {total_count} adresów IP.")

send_messages_in_lan()
