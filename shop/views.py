from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
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
    login_url = reverse_lazy('products')

class AboutView(TemplateView):
    template_name = "shop/about.html"