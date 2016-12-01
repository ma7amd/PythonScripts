"""
import urllib.request
from bs4 import BeautifulSoup



fhand = urllib.request.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_183148.html').read()
soup = BeautifulSoup(fhand, "html.parser")

tags = soup('span')


#num = [item.get_text() for item in soup.find_all("span", {"class": "comment"})]
num = [item.get_text() for item in tags]
count = 0
for i in num:
    count += int(i)
print(num)
print(count)

# Retrieve all of the anchor tags

for tag in tags:
   # Look at the parts of a tag
   print('TAG:', tag)
   print('URL:', tag.get('href', None))
   print('Contents:', tag.contents[0])
   print('Attrs:', tag.attrs)

##################################################


import urllib.request
from bs4 import BeautifulSoup


url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Dacia.html'
fhand = urllib.request.urlopen(url).read()      #reading the url

soup = BeautifulSoup(fhand, 'html.parser')      #the lib start the magic
tags = soup('a')                                #getting all tags starting with (a)
#print(tags)
for tag in tags:                #looping through the (a) tags
    h = tag.get('href', None)   #this loop will give me all http links
    print(h)
    str(h)                  #convert the steatment to a string
    h.rstrip()              #removing all white spaces from the end of the steatment
    spl = h.split('_')      #slicing the steatment by removing (_) and put all slices in a list
    lastwords = spl[-1]     #retriving the last item after slicing in the list we created
    if lastwords.startswith("M"):       #cheacking for the word beginning with (M)
        break
final = lastwords.split('.')            #slicing the steatment by removing (.) and put all slices in a list
print(str(final[0]))
"""
"""
import urllib.request
from bs4 import BeautifulSoup

lst = []

url1 = "http://python-data.dr-chuck.net/known_by_Dacia.html"

lst.append(url1)
print("Retrieving: ", url1)

fhand = urllib.request.urlopen(url1).read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('a')
url2 = tags[18]
href2 = url2.get("href", None)
lst.append(href2)
print("Retrieving: ", href2)

fhand = urllib.request.urlopen(href2).read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('a')
url3 = tags[18]
href3 = url3.get("href", None)
lst.append(href3)
print("Retrieving: ", href3)

fhand = urllib.request.urlopen(href3).read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('a')
url4 = tags[18]
href4 = url4.get("href", None)
lst.append(href4)
print("Retrieving: ", href4)


fhand = urllib.request.urlopen(href4).read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('a')
url5 = tags[18]
href5 = url5.get("href", None)
lst.append(href5)
print("Retrieving: ", href5)



fhand = urllib.request.urlopen(href5).read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('a')
url6 = tags[18]
href6 = url6.get("href", None)
lst.append(href6)
print("Retrieving: ", href6)



fhand = urllib.request.urlopen(href6).read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('a')
url7 = tags[18]
href7 = url7.get("href", None)
lst.append(href7)
print("Retrieving: ", href7)



fhand = urllib.request.urlopen(href7).read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('a')
url8 = tags[18]
href8 = url8.get("href", None)
lst.append(href8)
print("Last URL: ", href8)
print("Last Name: ", url8.contents[0])
"""

import urllib.request
from bs4 import BeautifulSoup
import json
import ssl


url1 = input("Enter URL: ")                                      #"http://python-data.dr-chuck.net/known_by_Dacia.html"
lst2 = list()
lst2.append(url1)

count = int(input("Enter Count: "))
position = int(input("Enter Position: "))

print("Retrieving: ", lst2[0])
for i in lst2:
    count -= 1
    if count > 0:
        #html = urllib.request.urlopen(lst2[-1]).read()
        scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        html = urllib.request.urlopen(lst2[-1], context=scontext)
        data = html.read()
        sop = BeautifulSoup(data, "html.parser")
        tagos = sop("a")
        a_tag = tagos[position - 1]
        hrf = a_tag.get("href", None)
        lst2.append(hrf)
        print("Retrieving: ", hrf)
        continue

    else:
        scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        html = urllib.request.urlopen(lst2[-1], context=scontext)
        data = html.read()
        sop = BeautifulSoup(data, "html.parser")
        tagos = sop("a")
        a_tag = tagos[position - 1]
        hrf = a_tag.get("href", None)
        lst2.append(hrf)
        print("Last URL: ", lst2[-1])
        print("Last Name: ", a_tag.contents[0])
        break
"""


import urllib.request
from bs4 import BeautifulSoup


url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Dacia.html'
fhand = urllib.request.urlopen(url).read()      #reading the url

soup = BeautifulSoup(fhand, 'html.parser')      #the lib start the magic
tags = soup('a')                                #getting all tags starting with (a)
#print(tags)
c = 0
for tag in tags:                #looping through the (a) tags
    c += 1
    print(tag)
    print(c)
"""