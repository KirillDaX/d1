from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import View, ListView
from django.views.generic.list import BaseListView

from cart.forms import ProductAddCartForm
from coresite.models import Product, Reviews, Article, Category


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 2
    template_name = 'index.html'
    queryset = Product.objects.order_by('-created_item').filter(available=True)[:50]
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = ProductAddCartForm().as_p()
        return context


def cart_view(request):
    return render(request, 'cart.html')


def product_detail(request, id, slug):
    """ вывод товара """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = ProductAddCartForm()
    return render(request, 'phone.html', {'product': product,
                                          'cart_product_form': cart_product_form})


class CategoryHierarchy(generic.ListView):
    """ отоборажение категорий  v2 """
    paginate_by = 2
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['hierarchy'])
        return Product.objects.filter(available=True, category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = ProductAddCartForm().as_p()
        return context


# class CategoryHierarchy(View):
#     """ отоборажение категорий """
#
#     def get(self, request, hierarchy=None):
#         return render(request,
#                       'index.html',
#                       {'categories': Category.objects.all(),
#                        'products': Product.objects.filter(available=True,
#                                                           category=get_object_or_404(Category, slug=hierarchy))})

# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'index.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})

# def category_hierarchy(request, hierarchy=None):
#     """ версия иерархии """
#     products = Product.objects.filter(available=True)[:50]  # ограничил показ на главной без категорий до 50
#     category = None
#     categories = Category.objects.all()
#     if hierarchy:
#         category_slugs = hierarchy.split('/')
#         categories_list = []
#         for slug in category_slugs:
#             if not categories_list:
#                 parent = None
#             else:
#                 parent = categories_list[-1]
#             category = get_object_or_404(Category, slug=slug, parent=parent)
#             categories_list.append(category)
#         # products = products.filter(category=category)  #так как результаты ограничены фильтр дальше работать не будет
#         products = Product.objects.filter(available=True, category=category)
#     return render(request,
#                   'index.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})
