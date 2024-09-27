# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.addons.ibjb_studio import common

class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    field_MqbX7 = fields.Char(
    	related="product_tmpl_id.default_code",
    	string="Product reference",
    	copy=False,
    	store=True,
    	readonly=False,
    )

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