from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('billing/', views.billing_page, name='billing'),
    path('invoice/', views.invoice, name='invoice'),
    path('stock/', views.stock, name='stock'),
    path('reports/', views.reports, name='reports'),
    
    # New API route
    path('lookup/', views.lookup_product, name='lookup'),
]
