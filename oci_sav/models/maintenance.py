# coding: utf-8

from odoo import fields, models


class MaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    maintenance_contact = fields.Many2one("res.partner", string="Client")
