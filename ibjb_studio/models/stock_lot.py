# -*- coding: utf-8 -*-

from odoo import fields, models


class StockLot(models.Model):
    _inherit = 'stock.lot'

    oci_lot_cout = fields.Float(
        string="Coût du lot",
        copy=False,
        store=True)
