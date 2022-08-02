import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.
from .forms import ToolForm, RegisterForm
from .models import Tool


def home(request):
    tools = Tool.objects.all()
    context = {'tools': tools,'added':request.GET.get('added',default=False)}
    return render(request, 'rental/home.html', context)


@login_required(login_url="/login")
def create_tool(request):
    if request.method == "POST":
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.owner = request.user
            tool.save()
            return redirect('/?added=true')
    else:
        form = ToolForm()
    for i in range(100000000):
        print()
    return render(request, "rental/createTool.html", {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {"form": form})
