# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ImmunoHemato(models.Model):
    _name = "immuno.hemato"
    _description = "This Model is Immuno hemato"

    name = fields.Char(string="Nom", copy=False, translate=False)
