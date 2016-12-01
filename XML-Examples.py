import xml.etree.ElementTree as ET

"""
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))
"""
#################################################################################
"""
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall("users/user")
print("User count:", len(lst))
for item in lst:
    print("Name", item.find("name").text)
    print("ID:", item.find("id").text)
    print("Attribute:", item.get("x"))

"""
###################################################################################

"""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved',len(data),'characters')
    print(data)
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat',lat,'lng',lng)
    print(location)
    """

    ###########################################################################

"""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET


serurl = "http://python-data.dr-chuck.net/comments_183145.xml"

url = urllib.request.urlopen(serurl).read()

tree = ET.fromstring(url)

lst = []
result = tree.findall(".//comment")
print("Retrieving: ", len(result))
for x in result:
    l = lst.append(x.find("count").text)
count = 0
coco = 0
for i in lst:
    count += int(i)
    coco += 1
print("Count: ", coco)
print("Sum: ", count)
"""

