from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact , About 
from blog .models import BlogPost



# Create your views here.

def home(request):
    # blog = BlogPost.objects.all()[:2]
    blog = BlogPost.objects.order_by('-publish_date')[:2]
    return render(request, "home/index.html",{"blog":blog})
    
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
    myabout = About.objects.all()
    return render(request, "home/about.html",{"myabout":myabout})
