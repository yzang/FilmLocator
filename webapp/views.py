import json

from django.http import HttpResponse
from django.shortcuts import render
from search import *


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def get_suggestion(request):
    response = ''
    if request.method == 'GET':
        query = request.GET['q']
        field = request.GET['f']
        items = elastic_suggest(query, field)
        data = {'items': items}
        response = json.dumps(data)
    return HttpResponse(response)
