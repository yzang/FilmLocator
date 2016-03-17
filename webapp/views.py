import json

from django.http import HttpResponse
from django.shortcuts import render
from search import *


# Create your views here.
from webapp.models import Film, Actor


def home(request):
    return render(request, 'index.html', {})


def search_film(request):
    response=''
    if request.method=='GET':
        params=request.GET
        filters=params.dict()
        print filters
        try:
            films=Film.objects.filter(**filters)
            response=json.dumps(films)
        except:
            pass
    return HttpResponse(response)


def get_suggestion(request):
    response = ''
    if request.method=='GET' and 'field' in request.GET:
        field=request.GET['field']
        if field!='actors':
            items=map(lambda x:x[field],Film.objects.values(field).distinct())
        else:
            items=map(lambda x:x['name'],Actor.objects.values('name').distinct())
        data={}
        data['items']=items
        response=json.dumps(data)
    return HttpResponse(response)
