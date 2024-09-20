# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons.ibjb_studio import common


class Partner(models.Model):
    _inherit = "res.partner"

    customer_code = fields.Char(string=(_("Code Tiers")), copy=False)

    customer_contact = fields.Char(string=(_("Contact")), copy=False)

    field_aD1p5 = fields.Selection(
        related="lang",
        help=(
            _(
                "All emails and documents sent to this contact will be translated into this language."
            )
        ),
        store=True,
        copy=False,
        readonly=False,
    )

    tva = fields.Char(string=(_("TVA")), copy=False)

    def Update_partner_studio_fields(self):
        """
        server action code to migrate partners studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_customer_code": "customer_code",
            "x_studio_customer_contact": "customer_contact",
            # 'x_studio_field_aD1p5': 'field_aD1p5', # No need to migarte this fields as it is related field
            "x_studio_tva": "tva",
        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
