# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common


class ContactRoles(models.Model):
    _name = "contact.roles"
    _description = "This Model is contact roles"

    name = fields.Char(string="Name")

    @api.model
    def migrate_contact_roles(self):
        """
        Scheduled action code to migrate Contact Roles data.
        """
        migration_fields = {
            "x_name": "name",
        }

        contact_roles = self.search([])

        for role in contact_roles:
            for x_field, field in migration_fields.items():
                common.set_customer_field(role, x_field, field)
