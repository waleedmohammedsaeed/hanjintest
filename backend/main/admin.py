from django.contrib import admin
from .models import Branch, Category, Services

# Register your models here.

admin.site.register(Branch)
admin.site.register(Category)
admin.site.register(Services)
