# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class ImmunoHemato(models.Model):
    _name = "immuno.hemato"
    _description = "This Model is Immuno hemato"

    name = fields.Char(string="Nom", copy=False)
