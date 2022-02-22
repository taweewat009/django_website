from django.contrib import admin
from .models import Blogs, PhotoAlbum,Comment,Customer

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','created_on','active')
    list_filter = ('active','created_on')
    search_filter = ('name','body')
    actions = ['approve_comments']

    def approve_comment(self,request,queryset):
        queryset.update(active=True)
    



class Design(admin.ModelAdmin):
    list_display = ["name","category","views"]



admin.site.register(Blogs,Design)
admin.site.register(PhotoAlbum)
admin.site.register(Customer)

