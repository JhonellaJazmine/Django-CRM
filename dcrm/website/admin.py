from django.contrib import admin
from .models import Record, Brand, Category, User, Role


admin.site.register(User)
admin.site.register(Record)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Role)

