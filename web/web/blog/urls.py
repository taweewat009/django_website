from django.urls import path
from .views import contact, index,blogdetail,about,contact,onlyme,sendwork,index2,sponsor,test_form



urlpatterns = [
    path('',index,name="index"),
    path('blogs',index2,name="blogs"),
    path('category/<slug:category_slug>',index,name="category"),
    path('<slug:slug>/',blogdetail,name="blogdetail"),
   
    #path('blog/<slug:slug>',blogdetail,name="blogdetail"),
    path('about/',about, name="about"),
    path('about/',contact,name="contact"),
    path('table',onlyme,name="onlyme"),
    # ช่องทางส่งงานนักเรียน ซ่อนลิงก์
    path('work',sendwork,name="work"),
    
    path('ads.txt',sponsor,name="spon"),
    path('test',test_form,name="test-form"),
]