from __future__ import unicode_literals

from django.shortcuts import render
from .models import form
from django.http import HttpResponse
from django.views.generic import View


#Creating our view, it is a class based view
# Create your views here.
def index(request):
    return render(request,'index.html')


def submit(request):
    if request.method == "POST" :
        gname = request.POST['gname']
        gfather = request.POST['gfather']
        bname = request.POST['bname']
        gaddress = request.POST['gaddress']
        bfather = request.POST['bfather']
        baddress = request.POST['baddress']
        name = request.POST['name']
        date = request.POST['date']
        rdate = request.POST['rdate']
        hello = form (gname = gname , gfather = gfather , bname = bname , gaddress = gaddress , bfather = bfather ,
        baddress = baddress , name = name , date = date , rdate = rdate )
        hello.save()
        return render(request,'submit.html', {'info':hello  })

    else :
        gname = request.GET['gname']
        gfather = request.GET['gfather']
        bname = request.GET['bname']
        gaddress = request.GET['gaddress']
        bfather = request.GET['bfather']
        baddress = request.GET['baddress']
        name = request.GET['name']
        date = request.GET['date']  
        id = request.GET['id']
        rdate = request.GET['rdate']
        hello = form (gname = gname , gfather = gfather , bname = bname , gaddress = gaddress , bfather = bfather ,
        baddress = baddress , name = name , date = date , id=id , rdate = rdate)


        return render(request,'submit.html', {'info':hello  })

def search(request):
    forms = form.objects.order_by('date')
    if 'id' in request.POST :
        id = request.POST['id']
        if id :
            forms = forms.filter(id=id)

    if 'gname' in request.POST :
        gname = request.POST['gname']
        if gname :
            forms = forms.filter(gname=gname)

    if 'gfather' in request.POST :
        gfather = request.POST['gfather']
        if gfather :
            forms = forms.filter(gfather=gfather)

    if 'bname' in request.POST :
        bname = request.POST['bname']
        if bname :
            forms = forms.filter(bname=bname)

    if 'date' in request.POST :
        date = str(request.POST['date'])

        if date :
            forms = forms.filter(date=date)



    context = {
    'forms' : forms ,
    }
    return render(request,'search.html',context)
