from collections import OrderedDict
from api.models import Product
from api.v1.subcategory.services import subcategory_format
from base.sqlpaginator import SqlPaginator
from sayt.settings import PER_PAGE


def product_pag(requests):
    tkan = Product.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page - 1) * limit
    print(tkan)
    result = []

    for i in range(offset, offset + limit):
        try:
            result.append(product_format(tkan[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(tkan))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_product(data):
    return OrderedDict([
        ("item", product_format(data)),
    ])


def product_format(data):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",data.subctg)
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('subctg', None if not data.subctg else subcategory_format(data.subctg)),
        ('discription', data.discription),
        ('brand', data.brand),
        ('on_complect', data.on_complect),
        ('uzunlik', data.uzunlik),
        ('kenglik', data.kenglik),
        ('balandlik', data.balandlik),
        ('img', data.img.url),
    ])
