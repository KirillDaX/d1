from django.shortcuts import get_object_or_404

from coresite.models import Category
from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}


def category(request):
    """ отображение категорий в dropdown - без подкатегорий"""
    categories = Category.objects.all()
    return {'categories': categories}





