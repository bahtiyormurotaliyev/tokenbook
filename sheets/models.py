from django.db import models



class Category(models.Model):
    categoryname = models.CharField(max_lenght=40, null=False, blank=False)

    def __str__(self) ->str:
          return self.categoryname

class Product(models.Model):
        name = models.CharField(max_length=40, null=True,blank=True)
        price = models.CharField(max_length=40,null=True, blank=True)
        quantity = models.IntegerField(blank=True, null=True)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name



class Harid(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='haridlar')
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.product_name}"