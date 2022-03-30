from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import ai_work
# Create your views here.
def index(request):
    return render(request,'vta/index.html')
def generateReplay(request):
    if request.method == 'POST':
        input_msg = request.POST['input_msg']
        reply = ai_work.keyboardInput(input_msg)
        print(reply)
        return HttpResponse(reply)
    return HttpResponse("Not a valid page")
