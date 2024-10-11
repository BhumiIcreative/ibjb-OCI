# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class ContactRoles(models.Model):
    _name = "contact.roles"
    _description = "This Model is contact roles"

    name = fields.Char(string="Name")
