# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common


class Regroupement(models.Model):
    _name = "regroupement.regroupement"
    _description = "This Model is regroupement"

    name = fields.Char(string="Name", copy=False)

    @api.model
    def migrate_regroupement_fields(self):
        print('\n\nMigrating regroupement fields...')

        # Mapping of old fields to new fields
        migration_fields = {
            "x_name": "name",  # Adjust this according to your field mappings
            # Add more field mappings if needed
        }

        # Fetch all regroupement records
        regroupement_records = self.search([])
        print('\nFetched regroupement records:', regroupement_records)

        for rec in regroupement_records:
            for x_field, field in migration_fields.items():
                # Assuming common.set_customer_field handles the field setting
                common.set_customer_field(rec, x_field, field)

