from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet
from .views import CategoryViewSet
from .views import ColorViewSet
from .views import SizeViewSet
from .views import CountryViewSet
from .views import BrandViewSet

router = SimpleRouter()
router.register('', ProductViewSet, basename='products')
router.register('category', CategoryViewSet, basename='categories')
router.register('colors', ColorViewSet, basename='colors')
router.register('size', SizeViewSet, basename='sizes')
router.register('country', CountryViewSet, basename='countries')
router.register('brand', BrandViewSet, basename='brands')
urlpatterns = router.urls
