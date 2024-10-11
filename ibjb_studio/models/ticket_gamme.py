# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields,api
from odoo.addons.ibjb_studio import common


class TicketGamme(models.Model):
    _name = 'ticket.gamme'
    _description = 'Ticket Gamme'

    name = fields.Char('Name')

    @api.model
    def migrate_ticket_gamme_fields(self):
        print('\n\n\n\nupdate_sale_studio_fields', self)
        """
        schedule action code to migrate ticket gamme studio fields data to custom fields.
        """
        migration_fields = {
            "x_name": "name",
        }
        ticket_gamme_orders = self.search([])
        print('\n\n\n\nsale_orders', ticket_gamme_orders)
        for rec in ticket_gamme_orders:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
