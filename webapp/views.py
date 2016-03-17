import json

from django.http import HttpResponse
from django.shortcuts import render
from search import *


# Create your views here.
from webapp.forms import FilterForm
from webapp.models import Film, Actor


def home(request):
    return render(request, 'index.html', {})


def search_film(request):
    response='{}'
    if request.method=='GET':
        form=FilterForm(request.GET)
        try:
            filters=form.get_filter()
            films=Film.objects.filter(**filters)
            data=[]
            for film in films:
                item=film.to_dict()
                data.append(item)
            response=json.dumps(data)
        except:
            pass
    return HttpResponse(response)


def get_suggestion(request):
    response = '{}'
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
