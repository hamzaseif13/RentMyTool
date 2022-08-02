from django.contrib.auth.views import LoginView
from django.urls import path
from .views import create_tool, sign_up, home
from .forms import CustomLoginForm
urlpatterns = [
    path("create-tool", create_tool, name="create_tool"),
    path('', home, name='home'),
    path('sign-up', sign_up, name='signup'),
    path('login/', LoginView.as_view(
        authentication_form=CustomLoginForm),
         name="login"
         ),


]
