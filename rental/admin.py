from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm, CustomUserChangeForm
from .models import *



admin.site.register(CustomUser)
admin.site.register(Tool)
admin.site.register(RentalDetails)