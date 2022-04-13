from rest_framework import routers
from products.views import ProductViewSet
from user_management.views import UserViewSet
router = routers.DefaultRouter()

# register routers
router.register('UserUpdate', UserViewSet)
router.register('productUpdate', ProductViewSet)

