#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:51:57 2024

@author: widhi
"""

import socket

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address (match serverUDP.py listening port 12345)
# Use docker compose service name for UDP server
server_address = ('udp-server', 12345)

# Send data to server
message = "Hello, UDP server2!"
client_socket.sendto(message.encode('utf-8'), server_address)

# Receive response from server
data, server = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode('utf-8')}")

# Send data to server (2)
message2 = "Im a College Student at Brawijaya University and my name is Eleazar Tadeo Eman!"
client_socket.sendto(message2.encode('utf-8'), server_address)

# Receive response from server (2)
data, server = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode('utf-8')}")

# Send data to server (3)
message3 = "This message here indicates that I successfully modified and use the code successfully!"
client_socket.sendto(message3.encode('utf-8'), server_address)

# Receive response from server (3)
data, server = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode('utf-8')}")

# Close the socket
client_socket.close()
