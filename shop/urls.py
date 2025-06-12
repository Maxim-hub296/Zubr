from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'shop'
urlpatterns = [
    path("", views.ProductsListView.as_view(), name="products"),
    path("<int:pk>/", views.ProductView.as_view(), name="product"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)