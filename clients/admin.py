from django.contrib import admin
from .models import Client, Project
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    # Form element order
    fields = ['name', 'description', 'avatar', 'date']
    # List element order
    list_display = ('name', 'date', 'description')


admin.site.register(Client, ClientAdmin)


class ProjectAdmin(admin.ModelAdmin):
    # Form element order
    # List element order
    list_display = ('name', 'client', 'url',
                    'platform', 'project_type')


admin.site.register(Project, ProjectAdmin)
