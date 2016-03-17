import json
import sys, os
import csv
import urllib2
import urllib
state='San Francisco, CA'
default_lat=37.7749295
default_lng=-122.4194155
django_home = "/home/ubuntu/django/FilmLocator"
sys.path.append(django_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

def clean(data):
    cleaned = data.strip().lower()
    if not cleaned or cleaned == 'na' or cleaned == 'n/a':
        return ''
    return data


if __name__ == '__main__':
    from webapp.models import Film, Actor

    reader = csv.reader
    with open('film_data.csv') as file:
        reader = csv.reader(file)
        # skil the header
        next(reader, None)
        for row in reader:
            if len(row) < 11:
                continue
            row=map(clean,row)
            title, year, location, facts, company, distributor, director, writer, actor1, actor2, actor3, _ = row
            actors = filter(clean, [actor1, actor2, actor3])
            if not location:
                continue
            # retry at most 3 times to get longitude and latitude
            latitude=default_lat
            longitude=default_lng
            for i in range(3):
                param = {"address": location + ' ' + state}
                request_url = 'https://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(param)
                response = urllib2.urlopen(request_url)
                google_data = json.load(response)
                if google_data['status'] == 'OK':
                    geolocation = google_data['results'][0]['geometry']['location']
                    latitude = geolocation['lat']
                    longitude = geolocation['lng']
                    break
            film=Film(title=title,year=year,location=location,facts=facts,
                      company=company,distributor=distributor,director=director,
                      writer=writer,latitude=latitude,longitude=longitude)
            for actor in actors:
                film.actors.add(Actor(actor))
            film.save()
