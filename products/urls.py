from django.urls import path, include
from rest_framework import routers
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    # path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    # path('product-list', views.ProductListAPIView.as_view(), name='product-list'),
    path('category-list', views.CategoryListView.as_view(), name='category-list'),
    # path('Pro-update/<int:pk>/', views.ProductUpdateView.as_view(), name='Pro-update'),
    # path('product-image/', views.ImageView.as_view(), name='image-upload'),
    path('pro_cat/<int:pk>/', views.product_category, name='pro-cat'),
    path('user_product/<int:pk>/', views.product_user, name='user_product'),

                  # path('product_images/<int:id>/', views.ProductImagesView.as_view(), name='pro-images'),
    # path('product_cat/<int:pk>/', views.ProducCategorytList.as_view(), name='product-cat'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
