# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common


class CodeAffaire(models.Model):
    _name = "code.affaire"
    _description = "This Model is code affair"

    name = fields.Char(string="Name", copy=False)


    @api.model
    def migrate_code_affaire(self):
        """
        Scheduled action code to migrate Code Affaire data.
        """
        migration_fields = {
            "x_name": "name",
        }

        affairs = self.search([])

        for affair in affairs:
            for x_field, field in migration_fields.items():
                common.set_customer_field(affair, x_field, field)
