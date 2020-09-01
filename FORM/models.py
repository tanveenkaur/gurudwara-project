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
    id = models.CharField(primary_key=True, editable=False, max_length=30)
    def save(self, **kwargs):
        if not self.id :
            max = (form.objects.aggregate(id_max=models.Max('id'))['id_max'])
            if max is not None:
                max = str(int(max)+1)
            else:
                max = 1

            self.id = str(max)
              # id from 100 to start
        super().save(*kwargs)
