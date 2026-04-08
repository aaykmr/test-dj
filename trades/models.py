from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    ORDER_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('EXECUTED', 'Executed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order_type} {self.quantity} {self.symbol} at {self.price}"

class Trade(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    executed_price = models.DecimalField(max_digits=10, decimal_places=2)
    executed_quantity = models.PositiveIntegerField()
    executed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trade for {self.order}"
