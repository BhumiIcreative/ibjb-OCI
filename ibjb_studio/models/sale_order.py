from odoo import fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    field_aueov_id = fields.Many2one(
        "maintenance.equipment", string=(_("Equipement de maintenance"))
    )
    # abonnement_equipement_id = fields.Many2one(
    #     "maintenance.equipment",
    #     string=(_("Maintenance Equipment")),
    #     ondelete="set null",
    #     copy=False,
    # )
