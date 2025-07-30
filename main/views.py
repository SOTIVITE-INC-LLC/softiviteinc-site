from django.shortcuts import render


def home(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def blog(request):
    return render(request, "main/blog.html")

def contact(request):
    return render(request, "main/contact.html")

def project(request):
    return render(request, "main/project.html")

def service(request):
    return render(request, "main/service.html")

def team(request):
    return render(request, "main/team.html")

def testimonial(request):
    return render(request, "main/testimonial.html")