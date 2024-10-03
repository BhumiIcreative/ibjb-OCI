# -*- coding: utf-8 -*-

from odoo import fields, models, _


class NafCode(models.Model):
    _name = "naf.code"
    _description = "This Model is NAF Code"

    name = fields.Char(string="Name")