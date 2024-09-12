# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class SaleOrderLine(models.TransientModel):
    _inherit = 'base.document.layout'

    legal_form = fields.Char()
    fax = fields.Char()
    siret = fields.Char()
    rcs = fields.Char()

