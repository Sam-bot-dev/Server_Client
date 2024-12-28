import socket

def start_client():
    host = '127.0.0.1'  # The IP of the server (localhost for local testing)
    port = 12345  # The same port that the server is listening on

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Message to send
    message = input("Enter here\n")

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive a response from the server (optional)
    response = client_socket.recv(1024)
    print(f"Server response: {response.decode()}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
