from django.contrib import admin
from django.urls import path, include
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('paypal/', include("paypal.standard.ipn.urls")),
    path('products/<int:id>/', views.products, name= 'products')
]
