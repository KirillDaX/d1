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
from django.urls import path
from django.conf.urls import include, url
import auth.views
import cart.views
import coresite.views
import orders.views
from main import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    # -- auth ----
    path('auth/', auth.views.auth_page, name='auth_page'),
    path('signup/', auth.views.signup, name='signup'),
    path('login/', auth.views.login_view, name='login'),
    path('logout/', auth.views.logout_view, name='logout'),
    # -- main page ---
    url(r'^', include('coresite.urls', namespace='coresite')),
    # -- cart ---
    path('cart/', include('cart.urls', namespace='cart')),
    # path(r'^cart/$', cart.views.cart_detail, name='cart'),
    # url(r'^remove/(?P<product_id>\d+)/$', cart.views.cart_remove, name='cart_remove'),
    # url(r'^add/(?P<product_id>\d+)/$', cart.views.cart_add, name='cart_add'),
    # url(r'^create/$', orders.views.order_create, name='order_create'),
    # -- ... ---

]

