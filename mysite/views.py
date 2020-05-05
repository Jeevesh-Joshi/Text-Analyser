# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # file_object = open("mysite\one.txt","r")

    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text')
    rmvpnc = request.POST.get('rmvpnc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if rmvpnc == 'on':
        for i in djtext:
            if i not in punctuations:
                analyzed += i

        djtext = analyzed

    if uppercase == 'on':
        analyzed = djtext.upper()
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if index == len(djtext)-1:
                break
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

    params = {'new_text': analyzed}

    return render(request,'analyze.html',params)
