from django.contrib import admin

# Register your models here.
from .models import Challenge,Tags

admin.site.register(Tags)
admin.site.register(Challenge)

