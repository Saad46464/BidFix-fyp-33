"""urls file."""
from django.urls import path
from . import views

urlpatterns = [
    path('offer-create', views.OffersListView.as_view(), name='offers-create'),
    path('offer/<int:pk>/', views.OfferProductListView.as_view(), name='offer'),
    path('Mycart/<int:pk>/', views.MycartProductListView.as_view(), name='Mycart'),
    path('pro_offers/<int:pk>/', views.product_offers, name='offers'),
]
