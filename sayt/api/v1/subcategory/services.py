from collections import OrderedDict
from api.models import SubCategory
from api.v1.category.services import category_format
from base.sqlpaginator import SqlPaginator
from sayt.settings import PER_PAGE


def subctg_pag(requests):
    tkan = SubCategory.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page - 1) * limit
    print(tkan)
    result = []

    for i in range(offset, offset + limit):
        try:
            result.append(subcategory_format(tkan[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(tkan))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_subctg(data):
    return OrderedDict([
        ("item", subcategory_format(data)),
    ])


def subcategory_format(data):
    return OrderedDict([
        ('id', data.id),
        ('content', data.content),
        ('ctg', None if not data.ctg else category_format(data.ctg)),
        ('img', data.img.url),
    ])
