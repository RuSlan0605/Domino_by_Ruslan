from django.urls import path
from shop.views import products_by_category

urlpatterns = [
	path('<slug:category_slug>/', products_by_category, name='by-category')
]