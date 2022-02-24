from django.urls import path
from .views import *



urlpatterns = [
    path('',index,name="index"),
    path('blogs',index2,name="blogs"),
    path('category/<slug:category_slug>',index,name="category"),
    path('<slug:slug>/',blogdetail,name="blogdetail"),
   
    #path('blog/<slug:slug>',blogdetail,name="blogdetail"),
    path('table',onlyme,name="onlyme"),
    # ช่องทางส่งงานนักเรียน ซ่อนลิงก์
    path('work',sendwork,name="work"),
    path('ads.txt',sponsor,name="spon"),
    path('test',test_form,name="test-form"),
    
    #path เกี่ยวกับ about ประวัติอะไรก็ตามขิงเว็บไซต์ ผู้เขียนเว็๋บ
    path('abouts',about,name='about'),
]