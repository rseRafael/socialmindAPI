from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import utils

makeFakeData = utils.makeFakeData
_msg = ""
_json = {}

@csrf_exempt
def generateFakeData(request):
    global _json, _msg, makeFakeData
    if request.method == "GET":
        try:
            makeFakeData()
        except Exception as err:
            print("Deu erro: ")
            print(err)
    _json['novo'] = "teste"
    response = JsonResponse(_json)
    response['Access-Control-Allow-Origin'] ="*"
    return response

