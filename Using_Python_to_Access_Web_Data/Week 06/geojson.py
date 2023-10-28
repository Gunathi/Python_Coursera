import urllib.request, urllib.error, urllib.parse
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI' #service url for the google maps api

while True:
    # address = input('Enter location: ') #Ask for the location
    # if len(address) < 1:
    #     break

    # url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving: ', serviceurl)
    uh = urllib.request.urlopen(serviceurl) #open the url
    data = uh.read().decode() #Read the whole document, because it is in the UTF-8 , decode the it to unicode
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) #loads the data into json format
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Fail to retrieve.....')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['result'][0]['geometry']['location']['lat']
    lng = js['result'][0]['geometry']['location']['lng']

    print('lat ', lat)
    print('lng ',lng)

    location = js['results'][0]['formatted_address']
    print(location)