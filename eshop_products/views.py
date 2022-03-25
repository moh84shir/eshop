from django.shortcuts import render
from django.views import generic
from .models import Product
from eshop_products_category.models import ProductCategory
from django.http import Http404


class ProductList(generic.ListView):
    queryset = Product.objects.get_active_products()
    paginate_by = 3


class ProductsListByCategory(generic.ListView):
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(
            name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)

from eshop_order.forms import UserNewOrderForm
def product_detail(request, pk):
    product = Product.objects.get_by_id(pk)
    product_categories = product.categories.all()
    form = UserNewOrderForm(request.POST or None)
    product.visit_count += 1
    product.save()

    context = {
        'product': product,
        'product_categories': product_categories,
        'form':form,
    }

    return render(request, 'eshop_products/product_detail.html', context)


class SearchProducts(generic.ListView):
    paginate_by = 3

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()
