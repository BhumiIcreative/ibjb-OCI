# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "BOY Stock Picking",
    "version": "17.0.1.0.0",
    "author": "Aktiv software",
    "summary": "Enhances stock picking with additional fields and functionality",
    "description": """This module adds additional fields to stock move and stock picking views, including:
        - Life date on stock move lines.
        - Actual lot ID and count of move lines on stock moves.""",
    "license": "LGPL-3",
    "depends": ["stock", "product_expiry"],
    "data": [
        "views/stock_move_line_views.xml",
        "views/stock_picking_views.xml",
    ],
}
