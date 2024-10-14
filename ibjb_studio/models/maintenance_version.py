# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.addons.ibjb_studio import common


class MaintenanceVersion(models.Model):
    _name = "maintenance.version"
    _description = "This Model is Maintenance Version"
    _rec_name = "name"

    name = fields.Char(string=(_("Name")))

    def Update_maintenance_version_studio_fields(self):
        """
            server action code to migrate Maintenance Version studio fields data to custom fields.
        """
        migration_fields = {
            "x_name": "name",
        }
        maintenance_version = self.search([])
        for rec in maintenance_version:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
