# -*- coding: utf-8 -*-

from odoo import fields, models, _


class NafCode(models.Model):
    _name = "naf.code"
    _description = "This Module is NAF Code"
    _rec_name = "name"

    name = fields.Char(string=(_("Name")))