from django.conf.urls import url
from django.urls import path

import cart.views
import orders.views

app_name = 'cart'
urlpatterns = [
    url(r'^$', cart.views.cart_detail, name='cart'),
    url(r'^remove/(?P<product_id>\d+)/$', cart.views.cart_remove, name='cart_remove'),
    url(r'^add/(?P<product_id>\d+)/$', cart.views.cart_add, name='cart_add'),
    url(r'^create/$', orders.views.order_create, name='order_create'),
]