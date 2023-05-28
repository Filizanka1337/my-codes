import socket
import threading

class Router:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.router_thread = threading.Thread(target=self.start_router)
    
    def start_router(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Router is running on {self.host}:{self.port}")
        
        while True:
            client_socket, client_address = self.sock.accept()
            self.clients.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
    
    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    self.broadcast(message, client_socket)
            except:
                self.clients.remove(client_socket)
                client_socket.close()
                break
    
    def broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.sendall(message.encode('utf-8'))
                except:
                    client.close()
                    self.clients.remove(client)

def main():
    router = Router('192.168.100.51', 5000)
    router.router_thread.start()

if __name__ == '__main__':
    main()
