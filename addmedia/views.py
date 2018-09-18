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
    global _msg
    _msg = ""
    global _result

    if request.method == "POST":
        if request.POST:
            _post = request.POST
            _mediaData = _post.get("mediaData")
            if _mediaData:
                _mediaData = json.loads(_mediaData)
                _startDate = formatISO(_mediaData['startDate'])
                _endDate = formatISO(_mediaData['endDate'])
                _mediaLink = _mediaData['mediaLink']
                if _startDate and _endDate:
                    if _mediaLink:
                        createNewMedia(_startDate, _endDate, _mediaLink)
                    else: 
                        _msg =  "mediaLink attribute is empty."
                else: 
                    _msg = "Data Format not allowed."
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

def createNewMedia(startDate, endDate, mediaLink):
    hasstarted, hasfinished = currentState(startDate, endDate)
    print(1)
    m = Media( startdate = startDate, enddate = endDate, link = mediaLink, hasstarted = hasstarted, hasfinished = hasfinished)
    m.save()
    print(2)

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