from django import forms
from django.forms import Textarea, TextInput, FileField, ClearableFileInput

from shop.models import Article, Customers


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","description","picture"]
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "picture": ClearableFileInput(attrs={"class":"form-control"})
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ["name","email","age"]
        widgets = {
            "name": TextInput(attrs={"class":"form-control"}),
            "email": TextInput(attrs={"class":"form-control"}),
            "age": TextInput(attrs={"class":"form-control"})
        }