from odoo import fields, models, api


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    aueov_sale_order_count = fields.Integer(string="Equipement de maintenance count")

    abonnement_equipement_sale_subscription_count = fields.Integer(string="Equipement de maintenance count",
                                                                   compute="_compute_sale_subscription_count",
                                                                   readonly=False)

    def _compute_sale_subscription_count(self):
        results = self.env['sale.order'].search(
            [('field_aueov_id', 'in', self.ids), ('is_subscription', '=', True)]
        )
        print("\n\n\nresult-------------->", results)

    def action_view_sale_order(self):
        pass

    def action_view_sale_subscription(self):
        pass
