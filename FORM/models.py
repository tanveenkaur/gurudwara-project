from django.db import models
from datetime import datetime



class form (models.Model):
    gname=models.CharField(max_length=50,default='SOME STRING')
    gfather=models.CharField(max_length=60,default='SOME STRING')
    name=models.CharField(max_length=50,default='SOME STRING')
    gaddress=models.CharField(max_length=250,default='SOME STRING')
    bname=models.CharField(max_length=50,default='SOME STRING')
    bfather=models.CharField(max_length=50,default='SOME STRING')
    baddress=models.CharField(max_length=250,default='SOME STRING')
    date = models.DateField()
    rdate = models.DateField()
    
