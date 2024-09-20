# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields


class ResCompany(models.Model):
    _inherit = 'stock.picking'

    is_expdition_bloque = fields.Boolean(_('Shipping blocked'))   # x_studio_expdition_bloque

