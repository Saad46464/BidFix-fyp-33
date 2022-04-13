from django.contrib import admin
from .models import *

#
# # class ProductFileAdmin(admin.StackedInline):
# #     model = ProductFile
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductFileAdmin]
#     class Meta:
#         model = Product
#
#
# @admin.register(ProductFile)
# class PictureInline(admin.ModelAdmin):
#     pass
#
#
admin.site.register(Product)
admin.site.register(Category)
