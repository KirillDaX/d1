"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static

import auth.views
import cart.views
import coresite.views
from main import settings

urlpatterns = [
    path('auth/', auth.views.auth_page, name='auth_page'),
    path('admin/', admin.site.urls),
    path('signup/', auth.views.signup, name='signup'),
    path('login/', auth.views.login_view, name='login'),
    path('logout/', auth.views.logout_view, name='logout'),
    path('', coresite.views.index_view, name='index'),
    path('index/', coresite.views.index_view, name='index'),
    path('cart/', cart.views.cart_detail, name='cart'),
    # url(r'^(?P<category_slug>[-\w]+)/$', coresite.views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', coresite.views.product_detail, name='product_detail'),
    # url(r'^$', coresite.views.ProductList, name='ProductList'),
    url(r'^remove/(?P<product_id>\d+)/$', cart.views.cart_remove, name='cart_remove'),
    url(r'^add/(?P<product_id>\d+)/$', cart.views.cart_add, name='cart_add'),
    # url(r'^$', cart.views.cart_detail, name='cart_detail'),
]
