# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models,api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # No need to migarte below fields as they are all related field

    oci_codedouane = fields.Char(
        related="product_template_id.article_codedouane",
        copy=False,
        readonly=True,
        store=False,
    )


    oci_bdc_comptecompt = fields.Char(
        related="product_id.property_account_income_id.display_name",
        string="Product reference",
        copy=False,
        readonly=True,
        store=False,
    )



