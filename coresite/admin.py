from django.contrib import admin
from coresite.models import Product, Reviews, Article

admin.site.register(Product)
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

