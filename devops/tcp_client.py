import socket

# Define server address and port
SERVER_HOST = '65.0.109.66'
SERVER_PORT = 5555

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send data to server
client_socket.sendall("Hello from client!".encode())

# Receive response from server
data = client_socket.recv(1024)
print("[*] Received from server:", data.decode())

# Close the connection
client_socket.close()