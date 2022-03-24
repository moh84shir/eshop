from django.shortcuts import render
from django.views import generic
from .models import Product
from eshop_products_category.models import ProductCategory


class ProductList(generic.ListView):
    queryset = Product.objects.get_active_products()
    paginate_by = 3


class ProductsListByCategory(generic.ListView):
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)


def product_detail(request, pk):
    product = Product.objects.get_by_id(pk)
    product_categories = product.categories.all()

    context = {
        'product': product,
        'product_categories': product_categories
    }

    return render(request, 'eshop_products/product_detail.html', context)
