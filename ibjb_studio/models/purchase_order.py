# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.addons.ibjb_studio import common


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    oci_achat_devis_codetiers = fields.Char(
        related="partner_id.customer_code",
        string="Code tiers",
        readonly=True,
        store=True,
        copy=False,
    )

    oci_achats_acheteur = fields.Many2one(
        "hr.employee",
        string="Buyer",
        copy=False,
        ondelete="set null",
    )

    def Update_purchase_order_studio_fields(self):
        """
        server action code to migrate Purchase studio fields data to custom fields.
        """
        migration_fields = {
            # "x_studio_customer_code": "oci_achat_devis_codetiers", # No need to migarte this fields as it is related field
            "x_studio_oci_achats_acheteur": "oci_achats_acheteur",
        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
