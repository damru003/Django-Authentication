from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from .forms import ImageForm
from .models import Image

def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        my_user = User.objects.create_user(name,email,password1)
        my_user.save()
        return redirect ('login')
    return render(request,"signup.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ('home')
        else:
            return HttpResponse ("Username or password is incorrect")
    return render(request, "login.html")


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render (request, "home.html",{'form':form, 'img':img})
