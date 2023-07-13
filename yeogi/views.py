from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def review_in_category(request, category) :
    current_category = None
    categories = Category.objacts.all()
#   review = Review.objects.filter(available_display = True)
    return render(request, 'yeogi/main.html', {'current_category':current_category, 'categories':categories, 'Review':Review})