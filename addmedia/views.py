from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from isoformat import formatISO
from . import models
import json

global Media
Media = models.Media
UpdateInfo  = models.UpdateInfo

@csrf_exempt
def add(request):
    global today
    global _msg
    global _result
    today = datetime.today()
    _msg = ""

    if request.method == "POST":
        if request.POST:
            _post = request.POST
            print(_post)
            _mediaData = _post.get("mediaData")
            if _mediaData:
                try:
                    _mediaData = json.loads(_mediaData)
                    _startDate = formatISO(_mediaData['startDate'])
                    _endDate = formatISO(_mediaData['endDate'])
                    _mediaLinks = _mediaData['mediaLinks']

                    if _startDate and _endDate:
                        if checkDate(_startDate, _endDate):
                            if _mediaLink:
                                createNewMedia(_startDate, _endDate, _mediaLinks)
                            else: 
                                _msg =  "mediaLink attribute is empty."
                        else:
                            _msg = "Start Date must be before {} and before End Data. Also, the difference between start and end date must be greater than thirty (30) minutes".format(today.isoformat())
                    else: 
                        _msg = "Data Format not allowed."
                except Exception as err:
                    _msg = err.args
            else: 
                _msg =  "POST body has no mediaData key."
        else:
            _msg =  "POST has no body."
    else:
        _msg = "Method is not POST."
        
    if _msg:
        _result = False
    else: 
        _result = True
        _msg = "New Media saved with success."
    _json = { 'result': _result,  'msg': _msg}
    response = JsonResponse(_json)
    response['Access-Control-Allow-Origin'] = "*"
    return response

# Create your views here.
def teste():
    _json = { 'result': False,  'msg': "qualquer coisa"}
    response = JsonResponse(_json)
    response['Access-Control-Allow-Origin'] = "*"
    return response

def createNewMedia(startDate, endDate, mediaLinks):
    for mediaLink in mediaLinks:
        hasstarted, hasfinished = currentState(startDate, endDate)
        m = Media( startdate = startDate, enddate = endDate, link = mediaLink, hasstarted = hasstarted, hasfinished = hasfinished)
        m.save()

def currentState(startDate, endDate):
    hasstarted = False
    hasfinished = False
    today = datetime.now()
    if today > startDate:
        hasstarted = True
    if today > endDate:
        hasfinished = False
    return (hasstarted, hasfinished)

def updateMediaState():
    try: 
        _objs = Media.objects.all()
        _lastID = _objs.last().id 
        '''
        for i in range(1, _lastID+1):
            _filter = _objs.filter(id = i)
            if _filter:
                _obj = _filter[0]
                started ,finished = currentState(_obj.startdate, _obj.enddate)
                _obj.hasstarted = started
                _obj.hasfinished = finished
        '''
        for _obj in _objs:
            started ,finished = currentState(_obj.startdate, _obj.enddate)
            _obj.hasstarted = started
            _obj.hasfinished = finished
            _obj.save()
        return True
    except Exception as err:
        return False

def checkUpdate():
    try:
        _today = datetime.today()
        _objs = UpdateInfo.objects.all()
        if len(_objs) < 1:
            _obj = UpdateInfo(lastupdate = _today)
        elif len(_objs) > 1:
            for _obj in _objs:
                _obj.lastupdate = _today
                _obj.save()
        else:
            _obj = _objs.all()[0]
            _obj.lastupdate = _today
            _obj.save()
    except Exception as err: 
         pass


def checkDate(startdate, enddate):
    today = datetime.today()
    if startdate < today:
        print("é antes de hoje")
        return False
    else:
        if startdate >= enddate:
            print("é antes de enddate")
            return False
        else:
            delta = enddate - startdate
            if delta.total_seconds() < 18000:
                print("a diferença é menor do que msg")
                return False
            else: 
                return True
