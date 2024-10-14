# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _,api
from odoo.addons.ibjb_studio import common


class EquipementCmf(models.Model):
    _name = "equipement.cmf"
    _description = "This Model is code equipement cmf"

    name = fields.Char(string="Name", copy=False)


    @api.model
    def migrate_equipement_cmf(self):
        """
        Scheduled action code to migrate Equipement CMF data.
        """
        migration_fields = {
            "x_name": "name",
        }

        equipement_records = self.search([])

        for equipement in equipement_records:
            for x_field, field in migration_fields.items():
                common.set_customer_field(equipement, x_field, field)
