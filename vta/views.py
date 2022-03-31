from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import ai_work
import pyttsx3
import speech_recognition as sr
# import gtts
# Create your views here.

def index(request):
    return render(request,'vta/index.html')

def generateReplay(request):
    if request.method == 'POST':
        input_msg = request.POST['input_msg']
        reply = ai_work.keyboardInput(input_msg)
        print(reply)
        try:
        	engine = pyttsx3.init()
        except Exception as e:
        	print(e)
        engine.say(reply)
        engine.runAndWait()
        del engine
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
