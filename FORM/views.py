from __future__ import unicode_literals

from django.shortcuts import render , get_object_or_404 , HttpResponseRedirect , redirect
from .models import form
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages


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
        y = date.split("-")
        date2 = y[2]+"-"+y[1]+"-"+y[0]
        z = rdate.split("-")
        date3 = z[2]+"-"+z[1]+"-"+y[0]
        return render(request,'submit.html', {'info':hello , 'dada' : date2 , 'dada1':date3})

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
        y = date.split("-")
        date2 = y[2]+"-"+y[1]+"-"+y[0]
        z = rdate.split("-")
        date3 = z[2]+"-"+z[1]+"-"+y[0]
        hello = form (gname = gname , gfather = gfather , bname = bname , gaddress = gaddress , bfather = bfather ,
        baddress = baddress , name = name , date = date2 , rdate = date3 , id=id)

        return render(request,'submit.html', {'info':hello , 'dada' : date , 'dada1':rdate })

def search(request):
    forms = form.objects.order_by('id')
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
        date = request.POST['date']

        if date :
            forms = forms.filter(date=date)


    context = {
    'forms' : forms ,
    }
    return render(request,'search.html',context)


def edit(request , id):
    form1=form.objects.get(pk=id)
    return render(request,'edit.html', {"form" : form1})


def update(request):
    if request.method == "GET" :
        gname = request.GET['gname']
        gfather = request.GET['gfather']
        bname = request.GET['bname']
        gaddress = request.GET['gaddress']
        bfather = request.GET['bfather']
        baddress = request.GET['baddress']
        name = request.GET['name']
        date = request.GET['date']
        y=date.split("-")
        z =y[2]+"-"+y[1]+"-"+y[0]
        rdate = request.GET['rdate']
        k=rdate.split("-")
        l =k[2]+"-"+k[1]+"-"+k[0]
        id=request.GET['id']
        hello = form (gname = gname , gfather = gfather , bname = bname , gaddress = gaddress , bfather = bfather ,
        baddress = baddress , name = name , date = z , rdate = l, id=id )
        hello.save()

        messages.success(request, 'Entry Updated')
        return render(request,'index.html')






def delete(request , id):
    if request.method =="GET":
        form1 = form.objects.get(pk=id)
        form1.delete()
        messages.success(request, 'Entry deleted')
        return render(request,'index.html')
