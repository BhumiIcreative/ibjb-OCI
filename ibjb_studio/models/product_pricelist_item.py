# -*- coding: utf-8 -*-
# from dataclasses import fieldss
from odoo import models, fields
from odoo.addons.ibjb_studio import common


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    field_MqbX7 = fields.Char(
        related="product_tmpl_id.default_code",
        string="Product reference",
        copy=False,
        store=True,
        readonly=False,
    ) # No need to migarte this fields as it is related field

    oci_pricelist_coms = fields.Text(
        string="New Multiline Text",
        copy=False,
        store=True,
    )

    saleorder_pricelist_productdate = fields.Char(
        string="New Text",
        copy=False,
        store=True,
    )

    def update_product_pricelist_studio_fields(self):
        print('\n\n\nselfupdate_product_pricelist_studio_fields',self)
        """
        server action code to migrate Product pricelist items studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_field_MqbX7":"field_MqbX7",
            # "x_studio_oci_pricelist_coms": "oci_pricelist_coms",
            "x_studio_studio_new_text":"saleorder_pricelist_productdate",
            "x_studio_x_studio_saleorder_pricelist_productdate": "saleorder_pricelist_productdate",
        }
        pricelist_item_orders = self.search([])
        for rec in pricelist_item_orders:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
