# coding: utf-8

from odoo import models, _


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    def get_opportunity_tags(self, helpdesktags):
        """
        Search for the crm tag same as helpdesk tags, if not found create one
        with name and color same as helpdesk tags
        returnType: list
        """
        opportunity = self.env["crm.tag"]
        update_tag_id = []
        for tag in helpdesktags:
            similar_tag = opportunity.search([("name", "=", tag.name)])
            if similar_tag:
                update_tag_id.append((4, similar_tag.id))
            else:
                new_tag = self.env["crm.tag"].create(
                    {"name": tag.name, "color": tag.color}
                )
                update_tag_id.append((4, new_tag.id))
        return update_tag_id

    def prepare_view_context(self):
        tag_ids = self.get_opportunity_tags(self.tag_ids)
        return {
            "search_default_partner_id": self.partner_id.id,
            "default_type": "opportunity",
            "default_partner_id": self.partner_id.id,
            "default_email_from": self.partner_email,
            "default_team_id": self.team_id.id,
            "default_name": self.name,
            "default_description": self.description,
            "default_tag_ids": tag_ids,
        }

    def action_opportunity_new(self):
        """
        Open new Opportunity form view with data from helpdesk ticket.
        """
        ctx = self.prepare_view_context()
        return {
            "name": _("Lead Converted"),
            "view_mode": "form",
            "res_model": "crm.lead",
            "type": "ir.actions.act_window",
            "context": ctx,
        }
