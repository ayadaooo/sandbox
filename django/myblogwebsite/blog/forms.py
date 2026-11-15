from django import forms
from .models import Post


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "border p-2 rounded w-full"}),
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "border p-2 rounded w-full"}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "border p-2 rounded w-full"})
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "border p-2 rounded w-full"}),
            "text": forms.Textarea(attrs={"class": "border p-2 rounded w-full"}),
        }
