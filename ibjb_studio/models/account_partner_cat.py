# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.addons.ibjb_studio import common


class AccountPartnerCat(models.Model):
    _name = "account.partner.cat"
    _description = "This Module is Third Party Accounting Category"

    name = fields.Char(string="Name")

    def Update_account_partner_cat_studio_fields(self):
        """
            server action code to migrate Account Partner Category studio fields data to custom fields.
        """
        migration_fields = {
            "x_name": "name",
        }
        account_partners = self.search([])
        for rec in account_partners:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)