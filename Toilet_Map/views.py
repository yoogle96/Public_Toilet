from django.shortcuts import render
from urllib.request import urlopen
import json

def home(request):
    with open('static/toilet.json') as json_file:
        json_data = json.load(json_file)
    
    return render(request, "index.html", context={'data':json_data['response']['body']['items']})

# Create your views here.
