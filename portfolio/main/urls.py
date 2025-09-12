from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("bio/", views.bio, name="bio"),
path("pitch/", views.pitch, name="pitch"),
path("contacts/", views.contacts, name="contacts"),
path("portfolio/<int:id>/", views.portfolio, name="portfolio"),


]