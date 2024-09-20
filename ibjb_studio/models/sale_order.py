from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    field_aueov_id = fields.Many2one("maintenance.equipment", string="Equipement de maintenance")
