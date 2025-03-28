from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from django.core.paginator import Paginator

from category.models import Category
from .models import Product, ProductImage, Region


def product_list(request):
    page = request.GET.get('page', 1)
    print('PAGE', page)
    products = Product.objects.prefetch_related(Prefetch('images',
            queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    paginator = Paginator(products, 2)
    page_obj = paginator.get_page(page)
    ctx = {
        "products": products,
        "page_obj": page_obj,
        'count': paginator.count
    }
    return render(request, 'products.html', ctx)


def product_detail(request, pk):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    product = Product.objects.prefetch_related('images').get(pk=pk)

    ctx = {
        "categories": categories,
        "regions" : regions,
        "product" : product
    }
    return render(request, 'detail.html', ctx)