# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# PORT = 80
# url = "http://data.pr4e.org/romeo.txt"
# HOST = url.split("/")[2]
# request = f"GET {url} HTTP/1.0\r\n\r\n"
# myText = b""
# try:
#     mysock.connect((HOST, PORT))
#     mysock.sendall(request.encode())
#     while True:
#         data = mysock.recv(500)
#         if len(data) < 1:
#             break
#         myText = myText + data
# except:
#     print("Something wrong")
# pos = myText.find(b"\r\n\r\n")
# print(myText.decode())
# myText = myText[pos + 4:].decode()
# print(myText)
