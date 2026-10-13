from django.db import models

# Create your models here.
from django.db import models

class FoodItem(models.Model):
    # 1. Primary key explicitly defined
    item_id = models.AutoField(primary_key=True)
    
    # 2. Name of the food item
    name = models.CharField(max_length=100)
    
    # 3. Category (e.g., Starters, Main Course, Dessert)
    category = models.CharField(max_length=50)
    
    # 4. Price of the item
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # 5. Customer rating (e.g., 4.5)
    rating = models.FloatField()
    
    # 6. Availability status
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.category})"