from django.contrib import admin
from django.contrib.auth.models import PermissionsMixin
from coresite.models import Product, Reviews, Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['available']
    # при добавлении 'created', 'updated'  выдает ошибку:
    # <class 'coresite.admin.ProductAdmin'>: (admin.E116)
    # The value of 'list_filter[1]' refers to 'created', which does not refer to a Field.
    # использовать PermissionsMixin или надо делать как кастомный фильтр?


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Reviews)
admin.site.register(Article)
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Reviews)
# class ReviewsAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass

