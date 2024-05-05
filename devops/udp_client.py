import socket

# Server configuration
SERVER_HOST = '65.0.109.66'  
SERVER_PORT = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send request to the server to get uptime data
client_socket.sendto('get_uptime'.encode(), (SERVER_HOST, SERVER_PORT))

# Receive response from the server
response, server_address = client_socket.recvfrom(1024)

# Decode and print the response
print(response.decode())

# Close the socket
client_socket.close()