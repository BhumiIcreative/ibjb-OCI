# -*- coding: utf-8 -*-

from odoo import fields, models, _


class MaintenanceVersion(models.Model):
    _name = "maintenance.etapes.pret"
    _description = "This Model is Maintenance Loan Steps"

    name = fields.Char(string="Name")
