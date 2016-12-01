import urllib.request
import urllib.parse
import json

serviseurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    adress = input("Enter Location: ")
    if len(adress) < 1 : break

    url = serviseurl + urllib.parse.urlencode({'sensor' : 'false', 'address' : adress})
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    

    try: js = json.loads(str(data.decode()))   #take care od the decode() function here in this line
    except: js =  None
    if js is None or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js["results"][0]["formatted_address"]
    print(location)

