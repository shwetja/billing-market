from django.contrib import admin

from .models import Product, ProductCategory, GST, Offer


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['product_name', 'product_category', 'product_cost_per_quantity', 'product_offer','product_total_cost']
admin.site.register(Product,  ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = ['catogery_name']
admin.site.register(ProductCategory,  ProductCategoryAdmin)

class GSTAdmin(admin.ModelAdmin):
    model = GST
    list_display = ['cgst', 'sgst', 'igst']
admin.site.register(GST,  GSTAdmin)

class OfferAdmin(admin.ModelAdmin):
    model = Offer
    list_display = ['offer_name']
admin.site.register(Offer,  OfferAdmin)