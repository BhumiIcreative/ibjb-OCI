# -*- coding: utf-8 -*-

from odoo import fields, models, _


class AccountPartnerCat(models.Model):
    _name = "account.partner.cat"
    _description = "This Module is Third Party Accounting Category"
    _rec_name = "name"

    name = fields.Char(string=(_("Name")))