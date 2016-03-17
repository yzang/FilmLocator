import json
import os,sys
from django.core.wsgi import get_wsgi_application

'''
This file is used to load json data into the Django database
Input: standard input with json format
'''

django_home = "/home/ubuntu/django/FilmLocator"
sys.path.append(django_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'FilmLocator.settings'

if __name__ == '__main__':
    application = get_wsgi_application()
    from webapp.models import Film, Actor
    for line in sys.stdin:
	print line
	j=json.loads(line)
	title=j['title']
	year=j['year']
	location=j['location']
	fact=j['fact']
	company=j['company']
	distributor=j['distributor']
	director=j['director']
	writer=j['writer']
	latitude=j['latitude']
	longitude=j['longitude']
	actors=j['actors']
        film=Film(title=title,year=year,location=location,fact=fact,
                  company=company,distributor=distributor,director=director,
            	  writer=writer,latitude=latitude,longitude=longitude)
	film.save()
        for name in actors:
	    actor,created=Actor.objects.get_or_create(name=name)
            film.actors.add(actor)
