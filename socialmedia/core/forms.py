from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
            'placeholder': "Enter your email here!",
        })
    )
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'block my-2 w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
            'placeholder': "Enter your first name here!",
        })
    )
    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'block my-2 w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
            'placeholder': "Enter your last name here!",
        })
    )
    bio = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'block my-2 w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
            'placeholder': "Enter your bio here!",
        })
    )
    dob = forms.DateField(
    label="",
    widget=forms.DateInput(
        attrs={
            'class': 'block my-2 w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
            'placeholder': "Select your date of birth",
            'type': 'date',
        }
    ),
    required=False
    )
    profile_image = forms.ImageField(
        label="Profile Image",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'block w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'bio', 'dob', 'email', 'first_name', 'last_name', 'password1', 'password2', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        # Username field
        self.fields['username'].widget.attrs['class'] = 'block w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="text-sm text-gray-500">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'

        # Password1 field
        self.fields['password1'].widget.attrs['class'] = 'block w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="text-sm text-gray-500 space-y-1">'
            '<li>Your password can\'t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can\'t be a commonly used password.</li>'
            '<li>Your password can\'t be entirely numeric.</li>'
            '</ul>'
        )

        # Password2 field
        self.fields['password2'].widget.attrs['class'] = 'block w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="text-sm text-gray-500">Enter the same password as before, for verification.</span>'
