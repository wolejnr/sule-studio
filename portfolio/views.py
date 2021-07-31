from django.shortcuts import render
from .models import Project, SocialMediaLink, Photo
from blog.models import Blog

# Create your views here.
def home(request):
    projects = Project.objects.all()
    blogs = Blog.objects.order_by('-blogdate')[:1]
    social_links = SocialMediaLink.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects, 'blogs':blogs, 'social_links': social_links})

def project(request):
    social_links = SocialMediaLink.objects.all()
    projects = Project.objects.all()
    photos = Photo.objects.all()
    return render(request, 'portfolio/project.html', {'social_links': social_links, 'projects': projects, 'photos': photos})