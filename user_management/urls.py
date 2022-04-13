from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import activate_user_view, password_reset_view,LogoutAPIView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/',  include('djoser.urls.jwt')),
    path('user_management/activate/<str:uid>/<str:token>/', activate_user_view),
    path('user_management/password/reset/confirm/<str:uid>/<str:token>/', password_reset_view),
    path('user_management/activate/<str:uid>/<str:token>/', activate_user_view),
    path('logout/', LogoutAPIView.as_view()),
    path('profile/update/<int:pk>/', views.UpdateManagement.as_view(), name='profile-crud')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

