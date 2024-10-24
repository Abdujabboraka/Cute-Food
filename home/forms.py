from .models import Food, Food_type
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms

# Create a custom login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Login view


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_type', 'name', 'ingredients', 'price', 'photo']
        widgets = {
            'food_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Name'}),
            'ingredients': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingredients'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'})
        }


class Food_typeForm(forms.ModelForm):
    class Meta:
        model = Food_type
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Type Name'}),
        }

