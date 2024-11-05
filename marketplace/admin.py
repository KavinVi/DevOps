from django.contrib import admin
from .models import Designer, Client, Project

# Register your models here.
admin.site.register(Designer)
admin.site.register(Client)
admin.site.register(Project)
