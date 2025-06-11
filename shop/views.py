from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.


class ProductsListView(ListView):
    template_name = "shop/products_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()


class ProductView(DetailView):
    template_name = "shop/product.html"
    model = Product
