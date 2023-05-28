import socket
import threading

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()
    
    def receive_messages(self):
        while True:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                print(message)
            except:
                print("Connection closed.")
                break
    
    def send_message(self, message):
        self.sock.sendall(message.encode('utf-8'))

def main():
    client = Client('159.205.215.95', 5000)
    while True:
        message = input()
        client.send_message(message)

if __name__ == '__main__':
    main()
