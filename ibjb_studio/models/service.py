# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common



class Service(models.Model):
    _name = "service.service"
    _description = "This Model is service"

    name = fields.Char(string="Name", copy=False)

    @api.model
    def migrate_service_fields(self):
        print('\n\nMigrating service fields...')

        migration_fields = {
            "x_name": "name",
        }
        # Fetch all service records
        service_records = self.search([])
        print('\n\n\nservice_records',service_records)

        for rec in service_records:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)

