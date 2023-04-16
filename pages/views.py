from django.shortcuts import render
from django.http import HttpResponse
from .models import Formulaire
def index(request):
    return render(request, 'pages\index.html')
def about(request):
    return render(request, 'pages\/about.html')
def contact(request):
    return render(request, 'pages\contact.html')
def home(request):
    return render(request, 'pages\home.html')
def formulaire(request):
    prenom1 = request.POST.get('prenom')
    email1 = request.POST.get('nom')
    montant1 = request.POST.get('montant')
    image1 = request.POST.get('image')
    data = Formulaire(prenom = prenom1, email = email1, montant = montant1, image = image1)
    data.save()
    return render(request, 'pages\/form.html')

# Create your views here.
