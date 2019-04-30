from django.shortcuts import render
from urllib.request import urlopen
import json

def test(request):
    return render(request, "test.html")

def home(request):
    url = 'http://api.data.go.kr/openapi/pblic-toilet-std?ServiceKey=GKrY0IlCVjdcT4cwBqkwS2Cwx9FFp7WGQRVApzmHKlhDqs8cz7swOzcUpzkEHZX6XV9TSC5YUqcM%2BtNLSndxQA%3D%3D&numOfRows=5&type=json'
    json_url = urlopen(url)
    json_data = json.load(json_url)
    print(type(json_data))
    # for i in range(0,300):
    #     print(i ,json_data['response']['body']['items'][i]['toiletNm'])
    return render(request, "index.html", context={'data':json_data['response']['body']['items']})

# Create your views here.
