from django.shortcuts import render, redirect
from .models import Message


def home(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def blog(request):
    return render(request, "main/blog.html")

def contact(request):
    return render(request, "main/contact.html")

def service(request):
    return render(request, "main/service.html")

def team(request):
    return render(request, "main/team.html")

def testimonial(request):
    return render(request, "main/testimonial.html")

def send_message(request):
    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        message = Message(
            email=email,
            message=message,
            subject=subject,
            phone=phone,
            name=name
        )
        message.save()
    return redirect("contact")