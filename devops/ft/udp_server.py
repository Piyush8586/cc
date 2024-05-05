[8:46 am, 05/05/2024] Shruti Modi: import socket

# Server configuration
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345      # Port to listen on
FILENAME = 'uptime_data.tsv'

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

print('Server is running and listening for requests...')

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)

    # Check if the client requested uptime data
    if data.decode().strip() == 'get_uptime':
        try:
            # Read uptime data from the file
            with open(FILENAME, 'r') as file:
                uptime_data = file.read()

            # Send uptime data to the client
            server_socket.sendto(uptime_data.encode(), client_address)
            print('Sent uptime data to', client_address)
        except FileNotFoundError:
            error_message = 'Error: Uptime data file not found.'
            server_socket.sendto(error_message.encode(), client_address)
            print('Error: Uptime data file not found.')
[8:46 am, 05/05/2024] Shruti Modi: Udp client Ani server