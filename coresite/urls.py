from django.conf.urls import url
import coresite.views

app_name = 'coresite'
urlpatterns = [
    url(r'^test/$', coresite.views.ProductListView.as_view(), name='test_view'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', coresite.views.product_detail, name='product_detail'),
    # url(r'^$', coresite.views.category_hierarchy, name='product_list'),
    # url(r'^category/(?P<hierarchy>.+)/', coresite.views.category_hierarchy, name='product_list_by_category')
    url(r'^$', coresite.views.ProductListView.as_view(), name='product_list'),
    url(r'^category/(?P<hierarchy>.+)/', coresite.views.CategoryHierarchy.as_view(), name='product_list_by_category')
]

# в шаблонах стоят product_list и product_list_by_category, по факту все объединил в category_hierarchy
# надо и в шаблонах поменять
