# -*- coding: utf-8 -*-


from odoo import fields, models, _


class MaintenanceVersion(models.Model):
    _name = "maintenance.version"
    _description = "This Module is Maintenance Version"
    _rec_name = "name"

    name = fields.Char(string=(_("Name")))
