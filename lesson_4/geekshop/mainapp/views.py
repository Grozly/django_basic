from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def main(request):
    title = 'Home, lesson_3'
    products_list = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products_list,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    title = 'Products, lesson_3'
    content = {
        'title': title,
        'links_menu': links_menu
        }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Contact, lesson_3',
    }
    return render(request, 'mainapp/contact.html', content)

