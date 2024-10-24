from django.contrib.auth import logout
from django.urls import path
from .views import homepage, food_form, food_typeform, edit_food, food_details, user_login, delete_food, register, \
    user_logout

urlpatterns = [
    path('home', homepage, name='homepage'),
    path('food-form/', food_form, name='food_form'),
    path('food-type-form/', food_typeform, name='food_type_form'),
    path('food-details/edit/<int:pk>', edit_food, name='edit_food'),
    path('/food-details/<int:pk>', food_details, name='food_details'),
    path('delete/<int:pk>', delete_food, name='delete_food'),
    path('', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),

    ]