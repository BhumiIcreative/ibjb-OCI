# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api
from odoo.addons.ibjb_studio import common


class HelpdeskSource(models.Model):
    _name = 'helpdesk.source'
    _description = 'Helpdesk Source'

    name = fields.Char()

    @api.model
    def migrate_helpdesk_source_fields(self):
        print('\n\nMigrating service fields...')

        migration_fields = {
            "x_name": "name",
        }
        # Fetch all service records
        helpdesk_source_records = self.search([])
        print('\n\n\nservice_records', helpdesk_source_records)

        for rec in helpdesk_source_records:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)


