# -*- coding: utf-8 -*-

from odoo import fields, models, _


class NafCode(models.Model):
    _name = "oci.helpdesk.type.ticket"
    _description = "This Module is helpdesk type ticket"

    name = fields.Char(string="Name")