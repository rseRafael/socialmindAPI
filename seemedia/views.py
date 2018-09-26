from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from addmedia.models import Media

@csrf_exempt
def getMedia():
    #Nothing till now