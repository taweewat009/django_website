from dataclasses import field
from tkinter.ttk import Widget
from django.forms import ModelForm, widgets

from .models import Comment, Customer


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
    

        

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
                