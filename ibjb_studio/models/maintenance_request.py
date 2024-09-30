# -*- coding: utf-8 -*-

from odoo import fields, models


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    pret_de_matriel_ = fields.Boolean(string="Need a loan of equipment ?")
    demande_de_pret_id = fields.Many2one("maintenance.request", string="Loan application")
    maintenance_contact = fields.Many2one("res.partner", string="Client")



