# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class EquipementCmf(models.Model):
    _name = "equipement.cmf"
    _description = "This Model is code equipement cmf"

    name = fields.Char(string="Name", copy=False)
