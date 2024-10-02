# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    legal_form = fields.Char(_('Legal form and capital'))
    fax = fields.Char(_('FAX'))
    rcs = fields.Char(_('RCS'))
