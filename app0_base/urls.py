from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('team', views.team, name='team'),
    path('expertise', views.expertise, name='expertise'),
    path('ai', views.ai, name='our ai'),
    path('contact', views.contact, name='contact'),
]