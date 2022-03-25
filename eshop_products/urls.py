from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('search/', views.SearchProducts.as_view(), name='search'),
    path('', views.ProductList.as_view(), name='list'),
    path('<int:pk>/', views.product_detail, name='detail'),
    path('<category_name>/', views.ProductsListByCategory.as_view(), name='category'),
]
