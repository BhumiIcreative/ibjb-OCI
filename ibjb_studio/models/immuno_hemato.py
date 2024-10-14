# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common


class ImmunoHemato(models.Model):
    _name = "immuno.hemato"
    _description = "This Model is Immuno hemato"

    name = fields.Char(string="Nom", copy=False)

    @api.model
    def migrate_immuno_hemato(self):
        """
        Scheduled action code to migrate Immuno Hemato data.
        """
        migration_fields = {
            "x_name": "name",
        }

        immuno_records = self.search([])

        for immuno in immuno_records:
            for x_field, field in migration_fields.items():
                common.set_customer_field(immuno, x_field, field)
