from django.contrib import admin

from core.loading import get_model
from .models import ProductRecord, UserRecord, UserSearch, UserProductView


class ProductRecordAdmin(admin.ModelAdmin):
    list_display = ('product', 'num_views', 'num_basket_additions',
                    'num_purchases')


class UserProductViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'date_created')


class UserRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'num_product_views', 'num_basket_additions',
                    'num_orders', 'total_spent', 'date_last_order')


admin.site.register(ProductRecord, ProductRecordAdmin)
admin.site.register(UserRecord, UserRecordAdmin)
admin.site.register(UserSearch)
admin.site.register(UserProductView, UserProductViewAdmin)
