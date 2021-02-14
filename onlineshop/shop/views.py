from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=categories)
        products = products.filter(category=current_category)
    return render(
        request,
        "shop/list.html",
        {
            "curent_category": current_category,
            "categories": categories,
            "products": products,
        },
    )
