# coding: utf-8

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    crm_helpdesk_ticket_id = fields.Many2one(
        "helpdesk.ticket", string=("Helpdesk ticket")
    )
