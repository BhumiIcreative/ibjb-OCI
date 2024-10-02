# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "BOY Sale Order",
    "version": "17.0.1.0.0",
    "author": "Aktiv software",
    "summary": " Enhances sale orders with additional lot features fields and functionality",
    "description": """This module extends the sale order functionality by adding custom fields and reports:
        - Life date on sale order lines.
        - Actual lot ID and count of move lines on order lines.""",
    "license": "LGPL-3",
    "depends": [
        "boy_company",
        'base',
        "sale",
        'sale_pdf_quote_builder',
        "boy_stock_picking",
        "delivery",
        "l10n_fr",
        "web"
    ],
    "data": [
        "views/sale_order_views.xml",
        "report/sale_order_report.xml",
        "report/sale_report.xml"
    ],
}
