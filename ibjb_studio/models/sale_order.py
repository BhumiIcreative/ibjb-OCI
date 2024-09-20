# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons.ibjb_studio import common


class SaleOrder(models.Model):
    _inherit = "sale.order"

    abonnement_equipement_id = fields.Many2one(
        "maintenance.equipment",
        string=(_("Maintenance Equipement")),
        ondelete="set null",
        copy=False,
    )

    def Update_sales_studio_fields(self):
        """
        server action code to migrate studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_abonnement_equipement": "abonnement_equipement_id",
        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
