from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
# Create your views here.
def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement_post.html')

def register(request):
    return render(request, 'redister.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def debug(request):
    for i in range(100):
        ad = Advertisement(
            title=f"Тестовое объявление {i}",
            text="Текст объявления",
            author="admin"
        )
        ad.save()
        ob = Advertisement.objects.all()
        print(ob)
    return HttpResponse("")