from django.contrib import admin
from .models import UploadedFile, User

admin.site.register(UploadedFile)

@admin.register(User)
class ModelNameAdmin(admin.ModelAdmin):
    pass




