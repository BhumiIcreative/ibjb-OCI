# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models,api
from odoo.addons.ibjb_studio import common


class ProductProduct(models.Model):
    _inherit = "product.product"

    categorie = fields.Char(
        related="categ_id.name",
        string="Category",
        store=True,
        copy=False,
        translate=True
    )

    @api.model
    def migrate_product_product_fields(self):
        migration_fields = {
            'x_studio_categorie': 'categorie',
        }

        product_products = self.search([])
        print('\n\n\nproduct_templates', product_products)  # Fetch all product templates
        for rec in product_products:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)