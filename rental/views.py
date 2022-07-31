from django.shortcuts import render

# Create your views here.
from .forms import ToolForm, RegisterForm


def home(request):
    return render(request,'rental/home.html')

def create_tool(request):
    if request.method=="POST":
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.owner= request.user
            tool.save()
    else :
        form = ToolForm()
    return render(request,"rental/createTool.html",{"form":form})

def sign_up(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request,'registration/signup.html', {"form":form })