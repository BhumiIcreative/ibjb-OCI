# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order'

    x_studio_purchase_order_reference = fields.Char(string=_('Purchase order reference'))
