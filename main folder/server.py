import socket

def start_server():
    host = '127.0.0.1'  # Localhost (you can use an IP address for remote communication)
    port = 12345  # Port to listen on

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP and port
    server_socket.bind((host, port))

    # Listen for incoming connections (max 5 clients)
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Receive the data from the client
        data = client_socket.recv(1024)  # Maximum data to receive is 1024 bytes
        print(f"Received message: {data.decode()}")

        # Send a response to the client (optional)
        client_socket.sendall("Message received!".encode())

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
