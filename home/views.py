from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact


# Create your views here.

def home(request):
    return render(request, "home/index.html")
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc","")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thanks = True
        return render(request, "home/contact.html", {"thanks": thanks})
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")
