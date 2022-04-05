from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import ai_work
import pyttsx3
import speech_recognition as sr
from django.contrib.auth.models import User
from .models import UploadQuestion, User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def index(request):
    return render(request,'vta/index.html')
    
@login_required(login_url='/')
def quizpaper(request):
    return render(request,'vta/quizpaper.html')
def uploadquestion(request):
    if request.method == "POST":
        subject_name = request.POST['subjectid']
        question_text = request.POST['questionid']
        optionA = request.POST['optiona']
        optionB = request.POST['optionb']
        optionC = request.POST['optionc']
        optionD = request.POST['optiond']
        correct_ans = request.POST['answerid']
        print(subject_name)
        UploadQuestion.objects.create(subject=subject_name,question=question_text,optionA=optionA,optionB=optionB,optionC=optionC,optionD=optionD,answer=correct_ans)
    return HttpResponse("Not a valid page")

@login_required(login_url='/')
def quiz(request,subject):
    questions = UploadQuestion.objects.filter(subject=subject)
    count = 0
    if request.method == "POST":
        print("INSIDE POST")
        for question in questions:
            print(type(question.id))
            ans = request.POST[str(question.id)]
            print(ans)
            if ans == question.answer:
                count+=1
            total_qns = len(questions)
            wrong_count = total_qns - count
            percentage = (count/total_qns)*100
        return render(request,'vta/results.html',{'total_qns':total_qns,'total':count,'wrong_count':wrong_count,'percentage':percentage,'subject':subject.capitalize()})
    return render(request,'vta/quizpage.html',{'questions': questions,'subject':subject,'csubject':subject.upper()})

def register(request):
    username_error = ""
    email_error = ""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        person_name = request.POST['person_name']
        account_type = request.POST['account_type']
        if User.objects.filter(username=username).exists():
            username_error = "Username already exists"
            return render(request,'register.html',{'username_error':username_error,'email_error':email_error})
        elif User.objects.filter(email=email).exists():
            email_error = "Email already exists"
            return render(request,'register.html',{'username_error':username_error,'email_error':email_error})
        user = User.objects.create_user(username, email, password)
        user.person_name = person_name
        if account_type == "faculty":
            user.is_faculty = True
        else:
            user.is_faculty = False
        user.save()
        login(request, user)
        return redirect('/home/')
    return render(request,'register.html',{'username_error':username_error,'email_error':email_error})

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
            engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
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
