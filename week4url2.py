import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 7
position = 18
url = 'http://py4e-data.dr-chuck.net/known_by_Leni.html'
for j in list(range(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    x = list()
    for tag in tags:
        x.append(tag.get('href', None))
    url = x[position-1]
    print(url)
    x.clear()
