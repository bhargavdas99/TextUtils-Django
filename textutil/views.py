from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    capitalize=request.POST.get('capitalize','off')
    lowercase=request.POST.get('lowercase','off')
    analyzed=djtext
    c=0
    if removepunc=='on':
        c+=1
        analyzed=''
        punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in djtext:
            if i not in punc:
                analyzed=analyzed+i
    if uppercase=='on':
        c+=1
        analyzed=analyzed.upper()
    if lowercase=='on':
        c+=1
        analyzed=analyzed.lower()

    if capitalize=='on':
        c+=1
        analyzen=''
        print(analyzed)
        print(len(analyzed))
        for j in range(len(analyzed)):
            if j==0:
                analyzen=analyzen+analyzed[j].upper()
            elif j>0 and analyzed[j-1]=='.':    
                analyzen=analyzen+analyzed[j].upper()
            else:
                analyzen=analyzen+analyzed[j].lower()
        analyzed=analyzen
    if c==0:
         params={
             'text':djtext
         }
         return render(request,"index1.html",params)
    else:    
        params={'analyzedText':analyzed}
        return render(request,"analyze.html",params)
