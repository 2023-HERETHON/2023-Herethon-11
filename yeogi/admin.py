from django.contrib import admin
from .models import Category, Review, Place, Street

# Register your models here.
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Place)
admin.site.register(Street)