from django.contrib import admin
from app_login import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Profile)