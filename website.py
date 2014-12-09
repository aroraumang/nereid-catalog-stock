# -*- coding: utf-8 -*-
"""
    website.py

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import PoolMeta

__metaclass__ = PoolMeta

__all__ = ['Product']


class Product:
    __name__ = 'product.product'
