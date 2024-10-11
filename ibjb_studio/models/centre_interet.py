# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class CentreInteret(models.Model):
    _name = "centre.interet"
    _description = "This Model is centre interet"

    name = fields.Char(string="Name", copy=False)
