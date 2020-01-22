from django.conf import settings
from coresite.models import Product
from decimal import Decimal


class Cart(object):
    """ класс для работы с корзиной через сессии. settings.CART_SESSION_ID = 'cart' """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}  # Сохраняем корзину в сессию
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """ Добавляем товар в корзину, обновляем количество. """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_sum_cart(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_sum_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear_cart(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
