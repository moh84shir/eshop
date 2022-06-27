from django.contrib import admin
from .models import Product, ProductComment


# register models
admin.site.register(Product)
admin.site.register(ProductComment)