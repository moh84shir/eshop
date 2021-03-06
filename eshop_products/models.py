from django.db import models
from django.db.models import Q
import os
from django.http import Http404
from django.contrib.auth import get_user_model
from eshop_products_category.models import ProductCategory


class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            raise Http404('محصولی یافت نشد')

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to="products/%M",
                              null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    categories = models.ManyToManyField(
        ProductCategory, blank=True, verbose_name="دسته بندی ها")
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')

    objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class ProductComment(models.Model):
    product:Product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    title = models.CharField(max_length=120, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    created = models.DateTimeField(verbose_name='زمان', auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='کاربر')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.product.__str__()
