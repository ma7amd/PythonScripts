import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time


'''
url = 'https://www.google.com/'
value = {
    "q": "python programming language"
}

data = urllib.parse.urlencode(value)
url = 'https://www.google.com/search?' + data
#data = data.encode('utf-8')


headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686)'
req =  urllib.request.Request(url, headers= headers)
res = urllib.request.urlopen(req)
res_data = res.read()

print(res_data)

'''

req = urllib.request.urlopen("http://www.nationaljournal.com/politics?rss=1")

xml = BeautifulSoup(req, 'xml')
for item in xml.findAll('link')[3:]:
    url = item.text
    news = urllib.request.urlopen(url).read()

    page = BeautifulSoup(news)

    for p in page.findAll('p'):
        print(p.text)

    time.sleep(10)