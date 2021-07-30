from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class SocialMediaLink(models.Model):
    twitter_url = models.URLField(max_length=300, blank=True)
    facebook_url = models.URLField(max_length=300, blank=True)
    instagram_url = models.URLField(max_length=300, blank=True)
    pinterest_url = models.URLField(max_length=300, blank=True)
    dribble_url = models.URLField(max_length=300, blank=True)
    linkedin_url = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return "Social Media Links"