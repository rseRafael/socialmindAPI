from addmedia.models import Media
from addmedia.views import mediatypes
import string
from string import ascii_letters, hexdigits
from random import random
from datetime import datetime, timedelta


def makeFakeData():
    lista = []
    for mediatype in mediatypes:
        qnt = round(random()*100 + 50)
        for i in range(qnt):
            mt = mediatype
            #mt = fakeMediaType()
            link = fakeLink(mt)
            sd, ed = fakeDate()
            hs, hf = fakeState(sd, ed)
            m = Media(link = link, startdate = sd, enddate = ed, hasfinished = hf, hasstarted = hs, mediatype = mt)
            m.save()


def fakeLink(mediatype):
    _strings = ascii_letters + hexdigits
    nLetters = round(random()*50 + 50)
    fakePart = ''
    for i in range(nLetters):
        try:
            randIndex = round(random()*(len(_strings)-1) )
            fakePart += _strings[randIndex]
        except Exception as err:
            pass
    link = "http://{0}.com/{1}".format(mediatype, fakePart)
    return link

def fakeDate():
    year = round(random())
    if year:
        year = 2019
    else:
        year = 2018
    month = round(random()*11 + 1)
    day = round(random()*27 + 1)
    delta = timedelta(random()*264 + 1)
    fakeStartDate = datetime(year, month, day)
    fakeEndDate = fakeStartDate + delta
    return (fakeStartDate, fakeEndDate)

def fakeState(startdate, enddate):
    today = datetime.today()
    if startdate > today:
        started  = False
    else:
        started = True
    if enddate > today:
        finished = False
    else:
        finished = True
    return (started, finished)

def fakeMediaType():
    index = round(random()*(len(mediatypes)-1))
    return mediatypes[index]


