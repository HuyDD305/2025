import urllib.request
import ssl
from bs4 import BeautifulSoup

# ignore SSL certificate errors
ctx = ssl.create_default_context()  # Creating the default SSL context
ctx.check_hostname = False  # Disable SSL hostname check
ctx.verify_mode = ssl.CERT_NONE  # Disable SSL certificate verification

if __name__ == "__main__":
    url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser"
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup("p")
    count = 0
    for tag in tags:
        count += 1

    print(count)



