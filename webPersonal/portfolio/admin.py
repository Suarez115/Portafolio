from django.contrib import admin
from .models import Proyect,ProjectImage
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')


class ProjectImageAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')

admin.site.register(Proyect,ProjectAdmin)
admin.site.register(ProjectImage,ProjectImageAdmin)