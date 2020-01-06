from django.shortcuts import render
from coresite.models import Product, Reviews, Article


# def home(request):
#     return render(request, 'auth_page.html')


def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def phone_view(request):
    return render(request, 'phone.html')


def cart_view(request):
    return render(request, 'cart.html')

# надо разобарться с отображением картинов в webp
