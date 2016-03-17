import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from webapp.forms import FilterForm
from webapp.models import Film, Actor

# The home page view
def home(request):
    return render(request, 'index.html', {})


# Provide service for searching and filtering films
def search_film(request):
    response = '{}'
    if request.method == 'GET':
        form = FilterForm(request.GET)
        try:
            filters = form.get_filter()
            if len(filters) == 0:
                response = get_all_films()
            else:
                films = Film.objects.filter(**filters)
                data = []
                for film in films:
                    item = film.to_dict()
                    data.append(item)
                response = json.dumps(data)
        except Exception, e:
            print str(e)
    return HttpResponse(response)


# Get all films and leverage the cache
def get_all_films():
    film_cache = cache.get('all_films')
    if film_cache:
        print "load from cache"
        return film_cache
    films = Film.objects.all()
    data = []
    for film in films:
        item = film.to_dict()
        data.append(item)
    film_json = json.dumps(data)
    cache.set('all_films', film_json)
    return film_json


# Get the suggestion list for auto complete, use cache if we can
def get_suggestion(request):
    response = '{}'
    if request.method == 'GET' and 'field' in request.GET:
        field = request.GET['field']
        cache_data = cache.get(field)
        if cache_data:
            response = cache_data
        else:
            if field != 'actors':
                items = map(lambda x: x[field], Film.objects.values(field).distinct())
            else:
                items = map(lambda x: x['name'], Actor.objects.values('name').distinct())
            data = {}
            data['items'] = items
            response = json.dumps(data)
            cache.set(field, response)
    return HttpResponse(response)
