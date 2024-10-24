from trace import Trace
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Food_type
from .forms import FoodForm, Food_typeForm, LoginForm
from django.contrib import messages



# Create your views here.
@login_required
def homepage(request):
    foods = Food.objects.all()
    food_types = Food_type.objects.all()
    context = {
        'foods': foods,
        'food_types': food_types,
    }
    return render(request, 'index.html', context)


@permission_required("home.change_food", raise_exception=True)
def food_form(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = FoodForm()
    return render(request, 'forms/food_form.html', {'form': form})


@permission_required("home.change_food_type", raise_exception=True)
def food_typeform(request):
    if request.method == 'POST':
        form = Food_typeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = Food_typeForm()
    return render(request, 'forms/food_type_form.html', {'form': form})


@permission_required("home.change_food", raise_exception=True)
def edit_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = FoodForm(instance=food)

    return render(request, 'forms/food_form.html', {'form': form})


@permission_required("home.delete_food", raise_exception=True)
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('homepage')

def food_details(request, pk):
    food = get_object_or_404(Food, id=pk)
    food.views += 1
    food.save()
    return render(request, 'detail/food_details.html', {'food': food})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                form.add_error(None, "Invalid username or password")  # Add error to the form
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

