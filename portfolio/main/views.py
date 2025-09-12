from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# Create your views here.
def home(request):
	return render(request, "home.html")

def bio(request):
	return render(request, "bio.html")


def portfolio(request, id):
	return render(request, "portfolio.html")


def pitch(request):
	return render(request, "pitch.html")


def contacts(request):
	return render(request, "contacts.html")