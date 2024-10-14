# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common


class AutomatesClient(models.Model):
    _name = "automates.client"
    _description = "This Model is code Automates client"

    name = fields.Char(string="Name", copy=False)


    @api.model
    def migrate_automates_client(self):
        """
        Scheduled action code to migrate Automates Client data.
        """
        migration_fields = {
            "x_name": "name",
        }

        clients = self.search([])

        for client in clients:
            for x_field, field in migration_fields.items():
                common.set_customer_field(client, x_field, field)
