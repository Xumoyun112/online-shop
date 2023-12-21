from django.shortcuts import render, HttpResponse
from .models import Category, Product


def home(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, slug):
    categorys = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=categorys)

    context = {
        'products': products
    }

    return render(request, 'shop/product_detail.html', context)


def about(request):
    return render(request, 'shop/about.html')
