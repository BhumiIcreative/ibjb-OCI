# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    abonnement_equipement_id = fields.Many2one(
        "maintenance.equipment",
        string=(_("Maintenance Equipement")),
        ondelete="set null",
        copy=False,
    )

    def Update_studio_fields(self):
        """
        server action code to migrate studio fields data to custom fields.
        """
        for rec in self:
            if hasattr(rec, "x_studio_abonnement_equipement"):
                rec.abonnement_equipement_id = rec.x_studio_abonnement_equipement.id
