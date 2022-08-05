from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Tool, RentalDetails

inputClass = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        exclude = ['last_rental', 'owner', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': inputClass,'required':True}),
            'status':forms.Select(attrs={'class':inputClass + "w-1/2"}),
            'description':forms.Textarea(attrs={'class':inputClass,'rows':'5','placeholder':'tell us about your tool, model, brand, year, features'}),
            'image_url':forms.URLInput(attrs={'class':inputClass}),
            'price':forms.NumberInput(attrs={'class':inputClass + "w-1/2",'min':0,'value':1})

        }



class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'required': True,
             'class': inputClass}
        )
        self.fields['last_name'].widget.attrs.update(
            {'required': True,
             'class': inputClass}
        )
        self.fields['username'].widget.attrs.update(
            {'required': True,
             'class': inputClass}
        )
        self.fields['email'].widget.attrs.update(
            {'required': True,
             'class': inputClass}
        )
        self.fields['password1'].widget.attrs.update(
            {'required': True,
             'class': inputClass}
        )
        self.fields['password2'].widget.attrs.update(
            {'required': True,
             'class': inputClass}
        )

    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", 'first_name', 'last_name']


class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "}
        )
        self.fields['password'].widget.attrs.update(
            {
                'class': "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "}
        )


class RentForm(forms.Form):
    rental_days = forms.IntegerField(max_value=14,min_value=1,widget=forms.NumberInput(attrs={'class':'rounded py-2 text-center font-bold ml-2','value':1}))



