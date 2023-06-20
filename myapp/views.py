from django.contrib.auth.models import User,  auth
from django.contrib import messages
from .models import Contactform, About, Projects, Contact, Social, Procent
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render, redirect

def index(request):
    social = Social.objects.all()
    return render(request, 'index.html', {'social' : social})

def about(request):
    about = About.objects.all()
    social = Social.objects.all()
    procent = Procent.objects.all()
    return render(request, 'about.html', { 'about' : about, 'social' : social, 'procent' : procent})

# def resume(request):
#     return render(request, 'resume.html')

def contact(request):
    con = Contact.objects.all()
    social = Social.objects.all()
    if request.method == "POST":
        contact = Contactform()
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact.name=name
        contact.email=email
        contact.message=message 
        contact.save()
        return HttpResponseRedirect("/")
    return render(request, "contact.html", {'con' : con, 'social' : social})


def portfolio(request): 
    project = Projects.objects.all()
    social = Social.objects.all()
    return render(request, 'portfolio.html', {'project' : project, 'social' : social})

