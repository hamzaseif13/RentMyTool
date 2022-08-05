import datetime
import time

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.
from .forms import ToolForm, RegisterForm, RentForm
from .models import Tool, RentalDetails, CustomUser


def home(request):
    tools = Tool.objects.all()  # Getting Available Tools only :)
    context = {'tools': tools}
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
    return render(request, "rental/createTool.html", {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        if request.user.is_authenticated: return redirect('/')
        form = RegisterForm()

    return render(request, 'registration/signup.html', {"form": form})


def tool(request, pk):
    try:
        tool = Tool.objects.get(pk=pk)
        if request.method == "POST":
            form = RentForm(request.POST)
            days = int(request.POST['rental_days'])
            if form.is_valid() and request.user.is_authenticated:
                return redirect(f'/?rented={tool.rent(request.user, days)}')
            else:
                return redirect('/')
        else:
            form = RentForm()
        return render(request, 'rental/tool.html', {'tool': tool, 'form': form})
    except Tool.DoesNotExist:
        raise Http404


def profile(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        tools = Tool.objects.filter(owner=user)
        historyRental=[]
        if request.user == user:
            historyRental = RentalDetails.objects.filter(renter=user)
    except CustomUser.DoesNotExist:
        raise Http404
    return render(request, 'rental/profile.html', {'historyRental': historyRental,'profile_user':user,'tools':tools})
