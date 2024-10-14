# -*- coding: utf-8 -*-

from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common


class NafCode(models.Model):
    _name = "oci.helpdesk.type.ticket"
    _description = "This Module is helpdesk type ticket"

    name = fields.Char(string="Name")

    @api.model
    def migrate_helpdesk_ticket_type(self):
        """
        Scheduled action code to migrate helpdesk ticket type data.
        """
        migration_fields = {
            "x_name": "name",
        }

        ticket_types = self.search([])

        for ticket in ticket_types:
            for x_field, field in migration_fields.items():
                common.set_customer_field(ticket, x_field, field)