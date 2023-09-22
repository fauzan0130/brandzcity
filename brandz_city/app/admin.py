from django.contrib import admin
from django.http import request
from .models import Contact, Customer, Product, Cart, OrderPlaced
from django.utils.html import format_html
from django.urls import reverse
from import_export.admin import ImportExportModelAdmin


admin.site.site_header = 'Brandz City'


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'phone_number',
                    'house_number', 'locality', 'landmark', 'city']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'description',
                    'original_price', 'price', 'category', 'product_img']

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change",
                       args=[obj.customer.pk])
        return format_html("<a href='{}'>{}</a>", link, obj.customer.name)

@admin.register(Cart)
class CartModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'user', 'customer_info', 'product_info', 'quantity', 'ordered_date', 'status']  # Add 'customer in the list to display full address in one line in admin panel.'

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change",
                       args=[obj.customer.pk])
        return format_html("<a href='{}'>{}</a>", link, obj.customer.name)
    
    def product_info(self, obj):
        link = reverse("admin:app_product_change",
                       args=[obj.product.pk])
        return format_html("<a href='{}'>{}</a>", link, obj.product)



@admin.register(Contact)
class ContactModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'contact_for', 'text']
