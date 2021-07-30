from django.shortcuts import render, get_object_or_404
from .models import Blog
from portfolio.models import SocialMediaLink

def all_blogs(request):
    blogs = Blog.objects.all()
    social_links = SocialMediaLink.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'social_links': social_links})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    social_links = SocialMediaLink.objects.all()
    return render(request, 'blog/detail.html', {'blog': blog, 'social_links': social_links})