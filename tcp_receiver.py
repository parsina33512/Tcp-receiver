import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('0.0.0.0', 8080)  # Listen on all interfaces, port 8080
print(f"Starting TCP server on {server_address[0]}:{server_address[1]}")
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")

        # Receive the data in small chunks
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received: {data.decode('utf-8')}")
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
        print("Connection closed.")