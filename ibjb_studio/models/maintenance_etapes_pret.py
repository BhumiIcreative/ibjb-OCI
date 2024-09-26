# -*- coding: utf-8 -*-

from odoo import fields, models, _


class MaintenanceVersion(models.Model):
    _name = "maintenance.etapes.pret"
    _description = "This Module is Maintenance Loan Steps"
    _rec_name = "name"

    name = fields.Char(string=(_("Name")))
