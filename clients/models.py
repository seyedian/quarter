from django.db import models
from django.utils import timezone
from settings.models import Platform, ProjectType
from PIL import Image
# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    avatar = models.ImageField(
        default='client_avatar.jpg', upload_to='media/avatars')
    description = models.CharField(max_length=100, blank=True, default='none')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    url = models.URLField(max_length=50, blank=False)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name
