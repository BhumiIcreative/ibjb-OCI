# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.addons.ibjb_studio import common


class LotMotifRetrait(models.Model):
    _name = 'lot.motif.retrait'
    _description = "Model for Stock Lot Withdrawal Reasons (Motif de Retrait)"

    name = fields.Char(string="Name")

    def Update_lot_motif_retrait_studio_fields(self):
        """
            server action code to migrate Stock Lot Withdrawal Reasons studio fields data to custom fields.
        """
        migration_fields = {
            "x_name": "name",
        }
        lot_motifs = self.search([])
        for rec in lot_motifs:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
