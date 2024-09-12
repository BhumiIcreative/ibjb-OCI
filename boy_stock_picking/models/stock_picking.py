# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models, _

log = logging.getLogger(__name__).info


class StockMove(models.Model):
    _inherit = 'stock.move'

    actual_lot_id = fields.Many2one('stock.lot', string=_('Actual lot'), compute='_get_lot_id')
    actual_lot_count = fields.Integer(
        string=_('Lot count'), compute='_cpt_actual_lot_count')

    life_date = fields.Datetime(string=_('Life date'), compute='_get_life_date')

    @api.depends('product_id')
    def _get_lot_id(self):
        """Compute the actual lot ID based on move lines."""
        for stock_move in self:
            if stock_move.move_line_ids:
                move_line = stock_move.move_line_ids[0]
                stock_move.actual_lot_id = move_line.lot_id
            else:
                stock_move.actual_lot_id = False

    @api.depends('actual_lot_id')
    def _get_life_date(self):
        """Compute the expiration date from the actual lot ID."""
        for stock_move in self:
            stock_move.life_date = stock_move.actual_lot_id.expiration_date

    @api.depends('product_id')
    def _cpt_actual_lot_count(self):
        """Compute the count of move lines associated with the stock move."""
        for stock_move in self:
            stock_move.actual_lot_count = len(stock_move.move_line_ids)
