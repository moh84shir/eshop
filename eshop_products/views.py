from django.shortcuts import render
from django.views import generic
from .models import Product, ProductComment
from eshop_products_category.models import ProductCategory
from django.http import Http404
from eshop_order.forms import UserNewOrderForm
from . import forms


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


def product_detail(request, pk):
    product = Product.objects.get_by_id(pk)
    product_categories = product.categories.all()
    product.visit_count += 1
    product.save()
    form = UserNewOrderForm(request.POST or None)
    product_comments = ProductComment.objects.filter(product=product).order_by('-pk')
    many = True


    if len(product_comments) <= 5:
        many = False

    comment_form = forms.AddCommentForm(request.POST)


    if comment_form.is_valid():
        cd = comment_form.cleaned_data
        ProductComment.objects.create(title=cd.get('title'), text=cd.get('text'), user=request.user, product=product)

    print(many)

    context = {
        'product': product,
        'comments': product_comments[:5],
        'product_categories': product_categories,
        'form':form,
        'many': many,
        'comment_form': comment_form,
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




# comments
def product_comment_list(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_comments = ProductComment.objects.filter(product=product)

    context = {
        'product': product,
        'comments': product_comments,
    }

    return render(request, 'eshop_products/product_comments.html', context)
