from django.shortcuts import *
from .models import *
from .forms import *

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def index(request):
	context = {
		'categories': Category.objects.all()
	}

	return render(
		request, 'shop/index.html', context
	)


def products_by_category(request, category_slug):
	products = get_list_or_404(
		Category,
		slug=category_slug
	)
