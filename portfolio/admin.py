from django.contrib import admin
from .models import Project, SocialMediaLink, Photo

# Register your models here.
admin.site.register(Project)
admin.site.register(SocialMediaLink)
admin.site.register(Photo)
