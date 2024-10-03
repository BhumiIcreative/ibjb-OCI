# -*- coding: utf-8 -*-

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