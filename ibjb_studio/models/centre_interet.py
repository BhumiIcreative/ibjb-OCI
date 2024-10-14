# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common


class CentreInteret(models.Model):
    _name = "centre.interet"
    _description = "This Model is centre interet"

    name = fields.Char(string="Name", copy=False)

    @api.model
    def migrate_centre_interet(self):
        """
        Scheduled action code to migrate Centre Interet data.
        """
        migration_fields = {
            "x_name": "name",
        }

        centres = self.search([])

        for centre in centres:
            for x_field, field in migration_fields.items():
                common.set_customer_field(centre, x_field, field)
