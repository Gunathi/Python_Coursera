import urllib.request, urllib.parse, urllib.error
import json
import ssl

#api_key = False
#if api_key is False:
#    api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
#else :
#    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    adress = input('Enter location: ')
    if len(adress) < 1:
        break
    url = serviceurl + urllib.parse.urlencode({'address': adress,'key': 42})
    print('Retreving:', url)
    urll = urllib.request.urlopen(url).read().decode()
    try:
        js = json.loads(urll)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK' :
        print('==Fail to retrieved==')
        print(urll)
        continue
    print(json.dumps(js, indent= 4))

    idd = js['results'][0]['place_id']
    print('Retrieved', len(urll), 'characters.')
    print('ID:',idd)

#Solution

# Enter location: Polytechnic University of Timisoara
# Retreving: http://py4e-data.dr-chuck.net/json?address=Polytechnic+University+of+Timisoara&key=42
# Retrieved 2716 characters.
# ID: ChIJA1RC_YJdRUcRespStH-z6us
