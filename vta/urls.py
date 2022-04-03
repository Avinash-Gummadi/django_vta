from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_request, name='login_request'),
    path('register/', views.register, name='register'),
     path('logout/',views.logout_view, name='logout'),
    # path('teacherRegister/', views.teacherRegister, name='teacherRegister'),
    path('home/', views.index, name='index'),
    path('home/quizpaper/', views.quizpaper, name='quizpaper'),
    path('home/uploadquestion/', views.uploadquestion, name='uploadquestion'),
    path('ai/', views.generateReplay, name='generateReplay'),
    path('speechToText/', views.speechToText, name='speechToText'),
]
