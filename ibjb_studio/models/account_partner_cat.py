# -*- coding: utf-8 -*-

from odoo import fields, models, _


class AccountPartnerCat(models.Model):
    _name = "account.partner.cat"
    _description = "This Module is Third Party Accounting Category"

    name = fields.Char(string="Name")