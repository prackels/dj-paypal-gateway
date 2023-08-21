from django.db import models
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.IntegerField()
    order_completed = models.BooleanField
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.order_id