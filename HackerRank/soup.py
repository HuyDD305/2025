import re  # Importing the 're' module to use regular expressions
import urllib.request  # Importing urllib to make HTTP requests
from bs4 import BeautifulSoup  # Importing BeautifulSoup for parsing HTML
import ssl  # Importing SSL to handle SSL certificate errors

# ignore SSL certificate errors
ctx = ssl.create_default_context()  # Creating the default SSL context
ctx.check_hostname = False  # Disable SSL hostname check
ctx.verify_mode = ssl.CERT_NONE  # Disable SSL certificate verification

def usingRegex(html):
    """This is a demo using regex"""
    # Using a regular expression to find all 'href' attributes that start with 'http' or 'https'
    links = re.findall(b'href="(http[s]?://.*?)"', html)
    for link in links:
        # Decode the bytes to a string and print each link
        print(link.decode())

def usingBeautifulSoup(soup):
    """This is a demo for using BeautifulSoup"""
    # Extracting all 'a' (anchor) tags from the parsed HTML
    tags = soup("a")
    for tag in tags:
        # For each 'a' tag, get the value of the 'href' attribute and print it
        print(tag.get('href', None))

if __name__ == "__main__":
    # Taking a URL input from the user
    url = input("Enter - ")
    # Opening the URL and reading the HTML content
    html = urllib.request.urlopen(url, context=ctx).read()
    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # Calling the usingRegex function to extract links using regular expressions
    usingRegex(html)
    print("----------------------------------------")
    # Calling the usingBeautifulSoup function to extract links using BeautifulSoup
    usingBeautifulSoup(soup)
