from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Video(models.Model):
    video = models.FileField(upload_to="videoes/", max_length=400, null=True, default=None)
    titel = models.CharField(max_length=500, null=True)
    slug_v = AutoSlugField(populate_from='titel', unique=True, null=True, default=None)


class Photo(models.Model):
    photo = models.ImageField(upload_to="photo/", null=True)