from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404


def main(request):
    title = 'Home, lesson_5'
    products_list = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products_list,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    title = 'Products, lesson_5'

    basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
            }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Contact, lesson_5',
    }
    return render(request, 'mainapp/contact.html', content)

