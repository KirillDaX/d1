from django.shortcuts import render, get_object_or_404
from coresite.models import Product, Reviews, Article


# def home(request):
#     return render(request, 'auth_page.html')


def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


# def phone_view(request):
#     return render(request, 'phone.html')


def cart_view(request):
    return render(request, 'cart.html')


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'phone.html', {'product': product})

# Страница с товарами
# def ProductList(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'shop/product/list.html', {
#         'category': category,
#         'categories': categories,
#         'products': products
#     })
