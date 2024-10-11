# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class Regroupement(models.Model):
    _name = "regroupement.regroupement"
    _description = "This Model is regroupement"

    name = fields.Char(string="Name", copy=False)
