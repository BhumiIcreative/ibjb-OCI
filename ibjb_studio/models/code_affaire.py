# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class CodeAffaire(models.Model):
    _name = "code.affaire"
    _description = "This Model is code affair"

    name = fields.Char(string="Name", copy=False)
