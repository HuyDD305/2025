# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# PORT = 80
# resource = b''
# while True:
#     url = input("Give me the link: ")
#     try:
#         aList = url.split("/")
#         HOST = aList[2]
#         mysock.connect((HOST, PORT))
#         request = f"GET {url} HTTP/1.0\r\n\r\n"
#         mysock.sendall(request.encode())
#         while True:
#             data = mysock.recv(1000)
#             if len(data) < 1:
#                 break
#             resource = resource + data
#             if len(resource.decode()) >= 3000:
#                 break
#         print(resource.decode())
#         print(len(resource.decode()))
#         x = input("Are you done: ")
#         if x == "yes":
#             break
#
#
#     except:
#         print("You enter wrong url or url not existed")
#         continue

