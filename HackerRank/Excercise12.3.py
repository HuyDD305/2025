import urllib.request
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()  # Creating the default SSL context
ctx.check_hostname = False  # Disable SSL hostname check
ctx.verify_mode = ssl.CERT_NONE  # Disable SSL certificate verification

url = input("Please give me the link")
fhand = urllib.request.urlopen(url, context=ctx)
data = b""

while True:
    info = fhand.read(10)
    if len(info) < 1:
        break
    data = data + info
    if len(data) >= 3000:
        break

print(data.decode())
print(len(data))



