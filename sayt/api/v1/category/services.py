from collections import OrderedDict
from api.models import Category
from base.sqlpaginator import SqlPaginator
from sayt.settings import PER_PAGE


def category_pag(requests):
    tkan = Category.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page - 1) * limit
    print(tkan)
    result = []

    for i in range(offset, offset + limit):
        try:
            result.append(category_format(tkan[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(tkan))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_category(data):
    return OrderedDict([
        ("item", category_format(data)),
    ])


def category_format(data):
    return OrderedDict([
        ('id', data.id),
        ('content', data.content),
        ('slug', data.slug),
        ('img', data.img.url),
    ])
