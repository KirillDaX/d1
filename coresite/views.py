from django.shortcuts import render, get_object_or_404

from cart.forms import ProductAddCartForm
from coresite.models import Product, Reviews, Article, Category


def index_view(request):
    products = Product.objects.all()

    cart_product_form = ProductAddCartForm()
    context = {'products': products,
               'cart_product_form': cart_product_form}
    return render(request, 'index.html', context)


def cart_view(request):
    return render(request, 'cart.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'index.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = ProductAddCartForm()
    return render(request, 'phone.html', {'product': product,
                                          'cart_product_form': cart_product_form})


