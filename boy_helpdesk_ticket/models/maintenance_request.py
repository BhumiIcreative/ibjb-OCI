# coding: utf-8

from odoo import fields, models


class MaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    maintenance_helpdesk_ticket_id = fields.Many2one(
        "helpdesk.ticket", string=("Helpdesk ticket")
    )
