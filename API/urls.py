from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet
from .views import ProductAPIView
from .views import CategoryAPIView
from .views import ColorAPIView
from .views import SizeAPIView
from .views import CountryAPIView
from .views import BrandAPIView


router = SimpleRouter()
router.register('', ProductViewSet, basename='products')

urlpatterns = [
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product_detail'),
    path('category/', CategoryAPIView.as_view(), name='categories'),
    path('color/', ColorAPIView.as_view(), name='colors'),
    path('size/', SizeAPIView.as_view(), name='sizes'),
    path('country/', CountryAPIView.as_view(), name='countries'),
    path('brand/', BrandAPIView.as_view(), name='brands'),
]
urlpatterns += router.urls
