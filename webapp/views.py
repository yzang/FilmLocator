import json

from django.http import HttpResponse
from django.shortcuts import render
from search import *


# Create your views here.
from webapp.models import Film, Actor


def home(request):
    return render(request, 'index.html', {})


def get_suggestion(request):
    response = ''
    if request.method=='GET':
        field=request.GET['field']
        if field!='actors':
            items=map(lambda x:x[field],Film.objects.values(field).distinct())
        else:
            items=map(lambda x:x[field],Actor.objects.values(field).distinct())
        data={}
        data['items']=items
        response=json.dumps(data)
    return HttpResponse(response)
