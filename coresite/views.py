from django.shortcuts import render, get_object_or_404

from cart.forms import ProductAddCartForm
from coresite.models import Product, Reviews, Article


def index_view(request):
    products = Product.objects.all()

    cart_product_form = ProductAddCartForm()
    context = {'products': products,
               'cart_product_form': cart_product_form}
    return render(request, 'index.html', context)


def cart_view(request):
    return render(request, 'cart.html')


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = ProductAddCartForm()
    return render(request, 'phone.html', {'product': product,
                                          'cart_product_form': cart_product_form})


