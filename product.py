# -*- coding: utf-8 -*-
"""
    product.py

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import PoolMeta

__metaclass__ = PoolMeta

__all__ = ['Website']


class Website:
    __name__ = 'nereid.website'

    buy_out_of_stock_products = fields.Boolean(
        'Allow buying out of stock products'
    )

    display_product_availability = fields.Boolean(
        'Display product availability'
    )

    @staticmethod
    def default_buy_out_of_stock_products():
        return True

    @staticmethod
    def default_display_product_availability():
        return False
