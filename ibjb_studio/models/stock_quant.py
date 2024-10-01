# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.addons.ibjb_studio import common


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    ref_interne_1 = fields.Char(
    	related="product_id.default_code",
    	readonly=True,
    	store=True,
    	copy=False,
    )

    field_WfwqV = fields.Datetime(
    	related='lot_id.expiration_date',
    	string="Expiration date",
    	readonly=True,
    	store=True,
    	copy=False,
    	help="This is the date on which the goods with this Serial Number may become dangerous and must not be consumed.",
    )

    oci_inventaire_note = fields.Text(
    	string="Possible Comment",
    	copy=False,
    	store=True,
    	tracking=True,
    )


    def Update_stock_quant_studio_fields(self):
        """
        server action code to migrate stock quant studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_oci_inventaire_note": "oci_inventaire_note",
        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
