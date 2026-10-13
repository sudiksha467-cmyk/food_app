from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FoodItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'name', 'category', 'price', 'rating', 'is_available')