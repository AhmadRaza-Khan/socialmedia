from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	title = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'block my-2 w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50', 'placeholder': "Enter your post title here!",}))
	content = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'block my-2 w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50', 'placeholder': "Enter your post content here!",}))
	image = forms.ImageField(label="Image", required=False, widget=forms.ClearableFileInput(attrs={'class': 'block w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',}))

	class Meta:
		model = Post
		exclude = ("user", "likes",)
		fields = ['title', 'content', 'image']