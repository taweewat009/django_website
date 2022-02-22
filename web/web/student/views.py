from django.shortcuts import render
from .models import Grade,Grade7,Grade8

# Create your views here.

def show_score(request):
    if 'q' in request.POST:
        q = request.POST['q']
        data = Grade.objects.filter(card_id=q)
        data_grade7 = Grade7.objects.filter(card_id=q)
        data_grade8 = Grade8.objects.filter(card_id=q)
    else:
        data = None
        data_grade7 = None
        data_grade8 = None
        
    return render(request, 'showscore.html',{'data':data,'data_grade7':data_grade7,'data_grade8':data_grade8})
