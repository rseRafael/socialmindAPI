from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from addmedia.models import Media
from urllib.parse import urlparse, parse_qs
from addmedia.views import mediatypes
import json
from datetime import datetime

_json ={}
_msg = ""
_result = False

@csrf_exempt
def getMedia(request):
    global _json, _msg, _result
    try:
        if request.method == "GET":
            _META = request.META
            if checkHttpReferer(_META):
                _path = request.get_full_path()
                _query = getQuery(_path)
                if _query:
                    _mediatype = _query['mediatype']
                    print("-_-_-_{0}-_-_-_-".format(_mediatype))
                    content  = Media.objects.filter(mediatype = _mediatype)
                    if len(content) > 0:
                        _result = True

                    else:
                        _msg="There is no media of type {0}".format(_mediatype)
                    
                else:
                    _msg= "QueryString is invalid."
            else:
                _msg= "HttpReferer: {0}. This server is not allowed.".format(_META.get('HTTP_REFERER'))
        else:
            _msg = "Request method must be GET not {0}".format(request.method)
    except Exception as err:
        qnt = 0
        errMsg = ""
        for prop in err.args:
            msg = "err.args[{0}] = {1}\n".format(qnt, prop)
            errMsg += msg
            qnt += 1
        _msg= "An error has occurred.\n" + errMsg
    print(_msg)
    fillJson()
    res = JsonResponse(_json)
    res['Access-Control-Allow-Origin'] = "*"
    return res

def checkHttpReferer(_META):
    referer = _META.get("HTTP_REFERER")
    if referer != None:
        if referer.find("http://localhost:4200/seemedia/options") != -1:
            return True
    return False

def checkQueryString(queryStr):
    if type(queryStr) == str:
        if queryStr.find('mediatype') != -1:
            for _type in mediatypes:
                if queryStr.find(_type) != -1:
                    return True
    return False

def getQuery(path):
    try:
        if type(path) == str:
            parsed = urlparse(path)
            if checkQueryString(parsed.query):
                query = parse_qs(parsed.query)
                print(query)
                for prop in query:
                    _list = query[prop]
                    if type(_list) == list and len(_list) > 0:
                        query[prop] = _list[0]
                return query
        return {}
    except Exception as err:
        return {}
            
def fillJson():
    global _msg, _result
    _json['message'] = _msg
    _json['result'] = _result

def classifyMedias(medias):
    _json = {}
    _json['completos'] = []
    _json['monitorando'] = []
    _json['futuro'] = []
    _json['erro'] = []
    _today = datetime.today()
    for media in medias:
        if media.hasstarted < today and media.hasfinished < today:
            _json['completos'].append(JsonfyMedia(media))

        else if media.hasstarted < today and media.hasfinished > today:
            _json['monitorando'].append(JsonfyMedia(media))

        else if media.hasstarted > today and media.hasfinished > today:
            _json['futuro'].append(JsonfyMedia(media))

        else if media.hasstarted > today and media.hasfinished < today:
            _json['erro'].append(JsonfyMedia(media))
        

def JsonfyMedia(media):
    _json = {}
    _json['link'] = media.link
    _json['startdate'] = media.startdate.isoformat()
    _json['enddate'] = media.enddate.isoformat()
    _json['hasstarted'] = media.hasstarted
    _json['hasfinished'] = media.hasfinished
    _json['mediatype'] = media.mediatype
    return json.dumps(_json)