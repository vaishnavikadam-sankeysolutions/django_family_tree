from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_initial_person, name='add_initial_person'),
    path('add_person/', views.add_person_api, name='add_person_api'),
]
