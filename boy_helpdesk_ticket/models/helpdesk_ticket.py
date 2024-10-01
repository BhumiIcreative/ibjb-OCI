# coding: utf-8

from odoo import api, fields, models, _
from math import ceil


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    open_on = fields.Datetime()

    @api.depends("close_date")
    def _compute_close_days(self):
        for ticket in self:
            ticket.close_days = 0
            if ticket.close_hours != 0:
                if ticket.close_date and ticket.open_on:
                    time_difference = fields.Datetime.from_string(
                        ticket.close_date
                    ) - fields.Datetime.from_string(ticket.open_on)
                    hours = ceil(
                        time_difference.days + (time_difference.seconds / 86400)
                    )
                    ticket.close_days = hours

    def _cpt_maintenance_request_count(self):
        for ticket in self:
            ticket.maintenance_request_count = len(ticket.maintenance_request_id)

    def _cpt_crm_lead_count(self):
        for ticket in self:
            ticket.crm_lead_count = len(ticket.crm_lead_id)

    close_days = fields.Integer(
        string=_("Close days"), default=0.0, compute=_compute_close_days
    )
    maintenance_request_count = fields.Integer(
        string=_("Maintenance request count"), compute=_cpt_maintenance_request_count
    )
    crm_lead_count = fields.Integer(
        string=_("CRM lead count"), compute=_cpt_crm_lead_count
    )

    maintenance_request_id = fields.One2many(
        "maintenance.request",
        "maintenance_helpdesk_ticket_id",
        string=_("Maintenance requests"),
    )
    crm_lead_id = fields.One2many(
        "crm.lead", "crm_helpdesk_ticket_id", string=_("CRM leads")
    )

    def open_customer_maintenance_request(self):
        return {
            "type": "ir.actions.act_window",
            "name": _("Maintenance requests"),
            "res_model": "maintenance.request",
            "view_mode": "kanban,tree,form,pivot,graph",
            "domain": [("id", "in", self.maintenance_request_id.ids)],
        }

    def open_customer_crm_lead(self):
        return {
            "type": "ir.actions.act_window",
            "name": _("CRM leads"),
            "res_model": "crm.lead",
            "view_mode": "kanban,tree,form,pivot,graph",
            "domain": [("id", "in", self.crm_lead_id.ids)],
        }

    def prepare_view_context(self):
        res = super(HelpdeskTicket, self).prepare_view_context()
        res.update(
            {
                "default_crm_helpdesk_ticket_id": self.id,
            }
        )
        return res
