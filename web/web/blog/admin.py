from django.contrib import admin
from .models import Blogs, PhotoAlbum,Comment,Customer

# Register your models here.
class Design(admin.ModelAdmin):
    list_display = ["name","category","views"]



admin.site.register(Blogs,Design)
admin.site.register(PhotoAlbum)
admin.site.register(Comment)
admin.site.register(Customer)

