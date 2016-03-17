import json
import sys, os
import csv
import urllib2
import urllib
import time

'''
This file will read input from film_data.csv and translate addresses into geolocation,
and generate output in json format
'''

state='San Francisco, '
default_lat=37.7749295
default_lng=-122.4194155

def clean(data):
    cleaned = data.strip().lower()
    if not cleaned or cleaned == 'na' or cleaned == 'n/a':
        return ''
    return data

def optimize_location(location):
    loc=location.replace("at","&")
    start=loc.find("(")
    end=loc.find(")",start)
    if start>=0 and end>=0:
	loc=loc[start+1:end]
    return state+loc

if __name__ == '__main__':
    reader = csv.reader
    with open('film_data.csv') as file:
        reader = csv.reader(file)
        # skil the header
        next(reader, None)
        for row in reader:
            if len(row) < 11:
                continue
            row=map(clean,row)
            title, year, location, fact, company, distributor, director, writer, actor1, actor2, actor3, _ = row
            actors = filter(clean, [actor1, actor2, actor3])
            if not location:
                continue
	    year=int(year)
            latitude=default_lat
            longitude=default_lng
	    # in case google api fails for limitations issue
            while True:
		time.sleep(0.13)
                param = {"address":optimize_location(location)}
                request_url = 'https://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(param)
                response = urllib2.urlopen(request_url)
                google_data = json.load(response)
                if google_data['status'] == 'OK':
                    geolocation = google_data['results'][0]['geometry']['location']
                    latitude = geolocation['lat']
                    longitude = geolocation['lng']
                    break
	    data={'title':title,'year':year,'fact':fact,'location':location,'company':company,'distributor':distributor,'director':director,'writer':writer,'actors':actors,'latitude':latitude,'longitude':longitude}
	    jsondata=json.dumps(data)
	    print jsondata
