from django.shortcuts import render # type: ignore
from app.forms import *
from django.http import HttpResponse # type: ignore
# Create your views here.
def insert_Topic(request):
    ETMFO=TopicModelForms()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        TMFDO=TopicModelForms(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Invalid')
    return render(request,'insert_Topic.html',d)

def insert_Webpage(request):
    EWMFO=WebpageModelForms()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WMFDO=WebpageModelForms(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Invalid')
    return render(request,'insert_Webpage.html',d)

def insert_AccessRecord(request):
    EARFO=AccessRecordModelForms()
    d={'EARFO':EARFO}
    if request.method=='POST':
        ARFDO=AccessRecordModelForms(request.POST)
        if ARFDO.is_valid():
            ARFDO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Invalid')
    return render(request,'insert_AccessRecord.html',d)

def wish(request,data):
    return HttpResponse(f' Hello {data} how are u')