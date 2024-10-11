# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class AutomatesClient(models.Model):
    _name = "automates.client"
    _description = "This Model is code Automates client"

    name = fields.Char(string="Name", copy=False)
