from django.contrib.auth.views import LoginView
from django.urls import path
from .views import create_tool, sign_up, home, tool, profile,update_tool,delete_tool,cancel_rental
from .forms import CustomLoginForm

urlpatterns = [
    path("create-tool", create_tool, name="create_tool"),
    path('', home, name='home'),
    path('sign-up', sign_up, name='signup'),
    path('login/', LoginView.as_view(
        authentication_form=CustomLoginForm),
         name="login"
         ),
    path('tool/<int:pk>', tool, name='tool'),
    path('profile/<str:username>', profile, name='profile'),
    path('tool/<int:pk>/update_tool',update_tool,name='update_tool'),
    path('tool/delete/<int:pk>',delete_tool,name='delete_tool'),
    path('rental/cancel/<int:pk>',cancel_rental,name='cance_rental')

]
