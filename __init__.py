# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from product import Product
from website import Website


def register():
    Pool.register(
        Product,
        Website,
        module='nereid_catalog_stock', type_='model'
    )
