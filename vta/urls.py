from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_request, name='login_request'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout_view, name='logout'),
    path('home/', views.index, name='index'),
    path('home/quizpaper/', views.quizpaper, name='quizpaper'),
    path('home/uploadquestion/', views.uploadquestion, name='uploadquestion'),
    path('home/quiz/<subject>/', views.quiz, name='quiz'),
    path('ai/', views.generateReplay, name='generateReplay'),
    path('speechToText/', views.speechToText, name='speechToText'),
]