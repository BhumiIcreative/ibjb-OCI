# -*- coding: utf-8 -*-
from odoo import fields, models, _
from odoo.addons.ibjb_studio import common


class SaleOrder(models.Model):
    _inherit = "sale.order"

    abonnement_equipement_id = fields.Many2one(
        "maintenance.equipment",
        string=(_("Maintenance Equipement")),
        ondelete="set null",
        copy=False,
    )  # sale_subscription field

    # No need to migarte below fields as they are all related field
    customer_vat = fields.Char(
        related="partner_id.tva",
        string=(_("Customer TVA")),
        readonly=True,
        copy=False,
        store=True,
    )
    oci_saleorder_codetiers = fields.Char(
        related="partner_id.customer_code",
        string=(_("Code tiers")),
        readonly=True,
        copy=False,
        store=True,
    )
    oci_vente_langcustomer = fields.Selection(
        related="partner_id.lang",
        string=(_("Customer language")),
        help=(
            _(
                "All emails and documents sent to this contact will be translated into this language."
            )
        ),
        store=True,
        copy=False,
        readonly=True,
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
