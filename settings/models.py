from django.db import models


class Platform(models.Model):
    platform_name = models.CharField(max_length=50, blank=False, unique=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.platform_name


class ProjectType(models.Model):
    project_type = models.CharField(max_length=50, blank=False, unique=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.project_type
