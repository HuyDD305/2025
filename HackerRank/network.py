# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')
# mysock.close()
#
# print(dir(mysock))

import socket
import time


import socket  # Import the socket library to work with network connections
import time    # Import time library to use sleep for slowing down recv()

HOST = "data.pr4e.org"  # The server domain name
PORT = 80               # HTTP standard port for web communication

# Create a socket object for IPv4 (AF_INET) and TCP (SOCK_STREAM)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the specified host and port
mysock.connect((HOST, PORT))

# Send an HTTP GET request to retrieve an image (cover3.jpg)
mysock.sendall(b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n")

count = 0      # To keep track of the total number of bytes received
picture = b""  # To accumulate the image data (binary string)

while True:
    data = mysock.recv(5100)  # Receive up to 5100 bytes of data from the server
    if len(data) < 1:         # If no data is received, the server has closed the connection
        break
    time.sleep(0.25)          # Slow down to give the server time to send more data
    count = count + len(data) # Update the byte count with the length of received data
    print(len(data), count)   # Print the length of current chunk and total received bytes
    picture = picture + data  # Append the received data to the picture variable

# Look for the end of the HTTP header (headers end with '\r\n\r\n')
pos = picture.find(b"\r\n\r\n")
print("Header length", pos)  # Print the position where the header ends
print(picture[:pos].decode())  # Print the HTTP header as a string (decoded from bytes)

# Skip past the header (position `pos`) and extract the image data
picture = picture[pos+4:]

# Open a file in binary write mode to save the image data
fhand = open("stuff.jpg", "wb")

# Write the binary image data to the file
fhand.write(picture)

# Close the file
fhand.close()
