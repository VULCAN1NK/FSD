from django.shortcuts import render,HttpResponse

# Create your views here.

def donor(request):
    return HttpResponse("I am a donor");