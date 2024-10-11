# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class Service(models.Model):
    _name = "service.service"
    _description = "This Model is service"

    name = fields.Char(string="Name", copy=False)
