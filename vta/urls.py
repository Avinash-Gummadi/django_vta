from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('ai/', views.generateReplay, name='generateReplay'),
    path('speechToText/', views.speechToText, name='speechToText'),
]
