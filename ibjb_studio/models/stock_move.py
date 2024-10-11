# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields,api
from odoo.addons.ibjb_studio import common


class StockMove(models.Model):
    _inherit = 'stock.move'

    codedouane_bl = fields.Char(_('Customs code'),related="product_id.product_variant_id.article_codedouane")  # x_studio_oci_codedouane_bl

    @api.model
    def migrate_stock_move_fields(self):
        print('\n\n\n\nmigrate_stock_move_fields', self)
        """
        schedule action code to migrate stock move studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_cha": "codedouane_bl"
        }
        stock_move_orders = self.search([])
        print('\n\n\n\nstock_move_orders', stock_move_orders)
        for rec in stock_move_orders:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)