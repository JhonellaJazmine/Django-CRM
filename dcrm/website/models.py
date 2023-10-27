from django.db import models
from django.contrib.auth.models import AbstractUser

# whatever database you use, same code lang rin
# django will make the class name plural

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True )
    email = models.EmailField(unique=True, null=True)
    roles = models.ManyToManyField(Role)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default="No description provided")
    # image = models.ImageField(null=True, default="image-svgrepo-com.svg")
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default="No description provided")

    def __str__(self):
        return self.name


class Product(models.Model):
    barcode = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    units_sold = models.PositiveIntegerField()

    def __str__(self):
        return self.name