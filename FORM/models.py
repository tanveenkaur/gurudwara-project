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
    date = models.CharField(max_length=16,default='SOME STRING')
    rdate = models.CharField(max_length=16,default='SOME STRING')
    id = models.CharField(primary_key=True, editable=False, max_length=30)
    def save(self, **kwargs):
        if not self.id :
            max =int (form.objects.aggregate(id_max=models.Max('id'))['id_max'])
            if max is not None:
                max += 1
            else:
                max = 1
            max = str(max)
            self.id = str(max)
              # id from 100 to start
        super().save(*kwargs)
