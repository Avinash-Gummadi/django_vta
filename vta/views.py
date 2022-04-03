from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import ai_work
import pyttsx3
import speech_recognition as sr
from django.contrib.auth.models import User
from .models import UploadQuestion, User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import user_passes_test
# import gtts
# Create your views here.
def auth(user):
   return user.is_authenticated

@user_passes_test(auth,login_url='/')
def index(request):
    return render(request,'vta/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        person_name = request.POST['person_name']
        account_type = request.POST['account_type']
        user = User.objects.create_user(username, email, password)
        user.person_name = person_name
        if account_type == "faculty":
            user.is_faculty = True
        else:
            user.is_faculty = False
        user.save()
        login(request, user)
        return redirect('/home/')
    return render(request,'register.html')

# def teacherRegister(request):
#     return render(request,'teacherRegister.html')

def login_request(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/home')
            else:
                error = "Invalid username or password"
        else:
            error = ""
        return render(request, 'login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('/')

def generateReplay(request):
    if request.method == 'POST':
        input_msg = request.POST['input_msg']
        soundstatus = request.POST['soundstatus']
        reply = ai_work.keyboardInput(input_msg)
        print(reply)
        if soundstatus == 'unmute':
            try:
            	engine = pyttsx3.init()
            except Exception as e:
            	print(e)
            engine.say(reply)
            engine.runAndWait()
            del engine
        elif soundstatus == 'mute':
            pass
        return HttpResponse(reply)
    return HttpResponse("Not a valid page")

def speechToText(request):
    if request.method == 'POST':
        speech = request.POST['speech']
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            r.pause_threshold=1
            audio= r.listen(source)
        try:
            print("Recognizing Voice!!!")
            query=r.recognize_google(audio,language="en-in")
            print(query)
        except Exception as e:
            print(e)
            query = "1"
            print("Say it again")
        return HttpResponse(query)
    return HttpResponse("Not a valid page")
