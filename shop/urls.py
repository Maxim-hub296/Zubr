from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path("", views.ProductsListView.as_view(), name="products"),
    path("<int:pk>/", views.ProductView.as_view(), name="product")
]