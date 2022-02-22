from django.urls import path
from .views import  index_Dash

urlpatterns = [
    path('index/dash',index_Dash,name="index-dash"),  # หน้าหลัก Dashboard 
]