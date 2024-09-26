# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields


class ResCompany(models.Model):
    _inherit = 'stock.move'

    codedouane_bl = fields.Char(_('Customs code'))  # x_studio_oci_codedouane_bl


