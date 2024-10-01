# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    life_date = fields.Datetime(string="Life date", compute="_get_life_date")

    @api.depends("lot_id")
    def _get_life_date(self):
        """compute the expiration date from the lot ID to the stock move line."""
        for stock_move_line in self:
            stock_move_line.life_date = stock_move_line.lot_id.expiration_date
