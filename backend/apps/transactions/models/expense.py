from django.db import models

from apps.transactions.models.category import Category
from utils.models import BaseModel
from django.contrib.auth.models import User


class Expense(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='expenses', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Expense of {self.amount} in {self.category.name} on {self.date.strftime('%Y-%m-%d')}"