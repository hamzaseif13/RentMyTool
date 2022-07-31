from django.urls import path
from .views import  create_tool,sign_up, home
urlpatterns=[
    path("create-tool",create_tool,name="create_tool"),
    path('',home,name='home'),
    path('signup',sign_up,name='signup')
]