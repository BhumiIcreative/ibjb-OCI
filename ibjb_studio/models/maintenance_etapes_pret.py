# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.addons.ibjb_studio import common


class MaintenanceEtapesPret(models.Model):
    _name = "maintenance.etapes.pret"
    _description = "This Model is Maintenance Loan Steps"

    name = fields.Char(string="Name")

    def Update_maintenance_etapes_pret_studio_fields(self):
        """
            server action code to migrate Maintenance Loan Steps studio fields data to custom fields.
        """
        migration_fields = {
            "x_name": "name",
        }

        maintenance_etapes = self.search([])
        for rec in maintenance_etapes:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
