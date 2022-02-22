from django.shortcuts import render

# Create your views here.

def index_Dash(request):
    return render(request,'Dashboard/index.html')
