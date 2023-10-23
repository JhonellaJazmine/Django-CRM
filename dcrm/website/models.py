# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

# whatever database you use, same code lang rin
# django will make the class name plural

# class CustomUserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("You have not provided a valid e-mail address")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user
    
#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
    
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, **extra_fields)
    
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(blank=True, default='', unique=True)
#     name = models.CharField(max_length=255, blank=True, default='')

#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(blank=True, null=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
    
#     def get_full_name(self):
#         return self.name

#     def get_short_name(self):
#         return self.name or self.email.split('@')[0]

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

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
    # roles = models.ManyToManyField(Role, related_name="records")


    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default="No description provided")

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