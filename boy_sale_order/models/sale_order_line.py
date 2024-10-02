# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    life_date = fields.Datetime(string=_('Life date'), compute='_get_life_date')
    lot_count = fields.Integer(
        string=_('Lot count'), compute='_cpt_lot_count')
    lot_id = fields.Many2one('stock.lot', string=_('Lot'), compute='_get_lot_id')

    @api.depends('lot_id')
    def _get_life_date(self):
        """Compute the expiration date based on the lot ID."""
        for order_line in self:
            order_line.life_date = order_line.lot_id.expiration_date

    @api.depends('product_id')
    def _get_lot_id(self):
        """Compute the lot ID based on associated move lines."""
        for record in self:
            if record.move_ids:
                for move_line in record.move_ids:
                    if move_line.actual_lot_id:
                        record.lot_id = move_line.actual_lot_id
                        break
                else:
                    record.lot_id = False
            else:
                record.lot_id = False

    @api.depends('product_id')
    def _cpt_lot_count(self):
        """Compute the count of lots based on associated move lines."""
        for record in self:
            lot_count = 0
            if record.move_ids:
                for move_line in record.move_ids:
                    if move_line.actual_lot_count is not None:
                        lot_count = move_line.actual_lot_count
                        break
            record.lot_count = lot_count
