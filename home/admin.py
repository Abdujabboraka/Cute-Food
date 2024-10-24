from django.contrib import admin
from .models import Food_type, Food



class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'food_type')

    class Meta:
        model = Food
        verbose_name = 'Taom'
        verbose_name_plural = 'Taomlar'

class Food_typeAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        model = Food_type
        verbose_name = 'Taom turi'
        verbose_name_plural = 'Taom turlari'

admin.site.register(Food, FoodAdmin)
admin.site.register(Food_type, Food_typeAdmin)
