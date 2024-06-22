from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
from django.contrib.auth import authenticate,login,decorators
from django.contrib.auth.decorators import login_required
from .models import post
from . import forms 
import datetime                                                                                      
# Create your views here.

@login_required
def home(request):
    user=request.user
    if user.is_authenticated: 
        content = post.objects.all().order_by("-created_at")
    else:
        content=None
   
    if request.method == 'POST':
        auther=user.username
        title=request.POST['title']
        dis=request.POST['description']
        new_user=post( auther=auther,title=title,description=dis)
        new_user.save()
        print('new post added')
        return redirect('home')

    return render(request,'index.html',{
        'content':content,
        'user':user,
        'forms':forms,
        })

def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,form.get_user())
                return redirect('home')
    else:
        form=AuthenticationForm() 
    return render(request,'login.html',{ 'form':form})

def user_logout(request):
    return render(request,'logout.html')

def user_signin(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect('home')
    else:
        form=UserCreationForm() 
    return render(request,'signin.html', { 'form':form})
 
def edit_post(request, post_id):
    print(post_id)
    Post_instance = get_object_or_404(post ,id=post_id)
    print(Post_instance)
    if request.method == "POST":
        form = forms.postForm(request.POST ,instance=Post_instance)
        if form.is_valid():  
            form.save()
            return redirect ("home")
    else:
        form = forms.postForm(instance=Post_instance)     
    return render (request , 'editpost.html',{'form':form})
