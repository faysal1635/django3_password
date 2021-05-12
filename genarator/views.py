from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'genarator/home.html',{'password':'adsjfkj'})

def password(request):
    thepassword = 'testing'
    character = list ('abcdefghigklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXZY'))

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))

    if request.GET.get('number'):
        character.extend(list('1234567890'))

    length = int(request.GET.get('length'))

    thepassword =''
    for x in range (length):
        thepassword += random.choice(character)
    return render(request,'genarator/password.html',{'password':thepassword})

def about(request):
    thename = 'Faysal'
    return render(request,'genarator/about.html',{'developer':thename})
