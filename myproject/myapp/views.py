from django.shortcuts import render, HttpResponse
from .models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.



def index(request):
    return render(request, 'index.html')
  
def experience(request):
    return render(request, 'experience.html')

def awards(request):
    return render(request, 'awards.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, contact=contact, message=message, date=datetime.now())
        contact.save()
        #messages.success(request, "Your message has been successfully sent.")
    return render(request, 'contact.html')
    