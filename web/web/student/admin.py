from django.contrib import admin
from .models import Grade,Grade7,Grade8
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

class GradeImport(ImportExportActionModelAdmin):
    list_display = ('card_id', 'name', 'subject1','subject2', 'comsci_score','comsci_Grade','tech_score','tech_Grade')

    
admin.site.register(Grade)
admin.site.register(Grade7,GradeImport)
admin.site.register(Grade8,GradeImport)