from django.contrib import admin
from .models import Note, TaskUser

admin.site.register(TaskUser)
admin.site.register(Note)


