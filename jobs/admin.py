from django.contrib import admin

# Register your models here.
from .models import Job, Resume

admin.site.register(Job)
admin.site.register(Resume)

