import json
import urllib2
import urllib
import time

'''
This file use Google Map Places API to get more accurate geolocation for some addressed
Input: standard input in json format
Output: standard output in json format, with location updated
'''

state = 'San Francisco, '
key = '<api key>'
reload(sys)
sys.setdefaultencoding('utf-8')


def optimize_location(location):
    loc = location.replace("at", "&")
    start = loc.find("(")
    end = loc.find(")", start)
    if start >= 0 and end >= 0:
        loc = loc[start + 1:end]
    return state + loc


for line in sys.stdin:
    obj = json.loads(line)
    location = obj['location']
    param = {"query": optimize_location(location), "key": key}
    request_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' + urllib.urlencode(param)
    response = urllib2.urlopen(request_url)
    google_data = json.load(response)
    if google_data['status'] == 'OK':
        geolocation = google_data['results'][0]['geometry']['location']
        latitude = geolocation['lat']
        longitude = geolocation['lng']
        obj['latitude'] = latitude
        obj['longitude'] = longitude
    print json.dumps(obj)
    time.sleep(0.15)
