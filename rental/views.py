import datetime
import time
12
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
        tool_history = RentalDetails.objects.filter(tool=tool)

        if request.method == "POST":
            form = RentForm(request.POST)
            days = int(request.POST['rental_days'])
            if form.is_valid() and request.user.is_authenticated:
                return redirect(f'/?rented={tool.rent(request.user, days)}')
            else:
                return redirect('/')
        else:
            form = RentForm()
    except Tool.DoesNotExist:
        raise Http404
    return render(request, 'rental/tool.html', {'tool': tool, 'form': form, 'tool_history': tool_history[::-1]})


def profile(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        tools = Tool.objects.filter(owner=user)
        historyRental = []
        if request.user == user:
            historyRental = RentalDetails.objects.filter(renter=user)
    except CustomUser.DoesNotExist:
        raise Http404
    return render(request, 'rental/profile.html',
                  {'historyRental': historyRental[::-1], 'profile_user': user, 'tools': tools})


def update_tool(request, pk):
    try:
        tool = Tool.objects.get(pk=pk)
        if not request.user == tool.owner:
            return redirect('/')
        if request.method == "POST":
            form = ToolForm(request.POST, instance=tool)
            # prevent tool from being edited if its currently rented
            if not tool.is_available:
                return redirect(F'/tool/{tool.id}?updated=false')
            if form.is_valid():
                form.save()
                return redirect(F'/tool/{tool.id}?updated=true')
        else:
            form = ToolForm(instance=tool)
    except Tool.DoesNotExist:
        raise Http404
    return render(request, "rental/update_tool.html", {"form": form, 'tool_id': tool.id})


def delete_tool(request, pk):
    tool = Tool.objects.get(pk=pk)
    deleted = 0
    if tool.is_available:
        deleted = tool.delete()[0]
    return redirect(f'/profile/{request.user.username}?deleted={deleted}')


def cancel_rental(request, pk):
    try:
        rental = RentalDetails.objects.get(pk=pk)
        rental.canceled = True
        rental.save()
        return redirect(f'/profile/{request.user.username}')
    except RentalDetails.DoesNotExist:
        return Http404
