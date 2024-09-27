# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # No need to migarte below fields as they are all related field
    oci_bdc_comptecompt = fields.Char(
        related="product_id.property_account_income_id.display_name",
        string="Product reference",
        readonly=True,
        copy=False,
    )
    oci_codedouane = fields.Char(
        related="product_template_id.article_codedouane",
        readonly=True,
        copy=False,
    )
