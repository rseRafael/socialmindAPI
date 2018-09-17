from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime as dt
from django.views.decorators.csrf import csrf_exempt
from isoformat import isoformat
import json
global times 
times = 1

@csrf_exempt
def add(request):
    global times
    print("Acesso: " + str(times))
    times += 1

    print("-----------------")
    for prop in dir(request):
        print(prop)
    print("-----------------")
    print("-----------------")
    print("META: ")
    print(request.META)
    print("GET:")
    print(request.GET)
    print("POST: ")
    print(request.POST)
    print("FILES: ")
    print(request.FILES)
    print("-----------------")
   
    today = dt.today()
    iso = today.isoformat()
    '''
    print("today: " + today.__str__())
    print("iso: " + iso)
    print(isoformat(iso))
    '''
    #tst = DT.fromisoformat(today.isoformat())
    myJson = { "resposta": True,  "maiscoisa": "bullshit"}
    print(myJson)
    res = JsonResponse(myJson)
    res['Access-Control-Allow-Origin'] = "*"
    return res

# Create your views here.
