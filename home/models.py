from django.db import models

# Create your models here.
class Food_type(models.Model):
    name = models.CharField(max_length=255, verbose_name='ovqat turi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Taom turi"
        verbose_name_plural = "Taom turlari"

class Food(models.Model):
    food_type = models.ForeignKey(Food_type, models.CASCADE, verbose_name='ovqat turi')
    name = models.CharField(max_length=255, verbose_name='nomi')
    ingredients = models.CharField(max_length=255, verbose_name='tarkibi')
    price = models.IntegerField(null=True, blank=True, verbose_name='narxi')
    photo = models.ImageField(upload_to='food-img/', blank=True, null=True, verbose_name='rasmi')
    views = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name="ko'rislar")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Taom"
        verbose_name_plural = "Taomlar"