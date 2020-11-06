import random
from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404


def get_hot_product():
    product_items = Product.objects.all()
    return random.sample(list(product_items), 1)[0]


def get_some_products(hot_product):
    some_products = Product.objects.filter(category_id=hot_product.category_id).exclude(pk=hot_product.pk)[:4]
    return some_products


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def main(request):
    title = 'Home, lesson_6'
    products_list = Product.objects.all()[:4]
    basket = get_basket(request.user)
    content = {
        'title': title,
        'products': products_list,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    title = 'Products, lesson_6'
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products_item = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_item = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_item,
            'basket': basket,
            }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_some_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    basket = get_basket(request.user)
    content = {
        'title': 'Contact, lesson_6',
        'basket': basket,
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    basket = get_basket(request.user)
    product_items = get_object_or_404(Product, pk=pk)
    print(product_items)
    # same_products = get_some_products(product_items)
    content = {
        'title': 'Product, lesson_6',
        'product': product_items,
        # 'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/product_deails.html', content)


def not_found(request, exception):
    basket = get_basket(request.user)
    title = 'Страница не найдена'
    content = {
        'title': title,
        'product_item': Product.objects.all[:4],
        'basket': basket,
    }
    return render(request, 'mainapp/404.html', content)

