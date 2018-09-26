from django.db import models
    
class Media(models.Model):
    link = models.CharField(max_length=1000, null=True, blank=True)
    startdate = models.DateTimeField(null=True, blank=True)
    enddate = models.DateTimeField(null=True, blank=True)
    hasfinished = models.BooleanField(null = True, blank= True) 
    hasstarted = models.BooleanField(null = True, blank=True)
    mediatype = models.CharField(max_length=1000, null=True, blank=True)
# Create your models here.


class UpdateInfo(models.Model):
    lastupdate = models.DateTimeField(null=True, blank = True)
    