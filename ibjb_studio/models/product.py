# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    categorie = fields.Char(
        related="categ_id.name",
        string="Category",
        store=True,
        copy=False,
        translate=True
    )