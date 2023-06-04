from django.shortcuts import render,redirect
from django.contrib import messages
from home.models import *


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')

        data = Contact(
            name = fname,
            email = femail,
            phonenumber = fphoneno,
            description = fdesc
        )
        data.save()

        messages.success(request, 'Thanks for contacting us..')
        messages.success(request, 'Thanks for contacting us..')
    return render(request, 'contact.html')


def about(request):
    views = {}
    views['informations'] = About.objects.all()
    return render(request, 'about.html', views)


def handleblog(request):
    views = {}
    views['posts'] = Blog.objects.all()

    return render(request, 'handleblog.html', views)




