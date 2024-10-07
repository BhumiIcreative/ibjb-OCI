# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.addons.ibjb_studio import common


class NafCode(models.Model):
    _name = "naf.code"
    _description = "This Model is NAF Code"

    name = fields.Char(string="Name")

    def Update_naf_code_studio_fields(self):
        """
            server action code to migrate Naf Code studio fields data to custom fields.
        """
        migration_fields = {
            "x_name": "name",
        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)