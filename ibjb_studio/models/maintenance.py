# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    aueov_sale_order_count = fields.Integer(
        string="Equipement de maintenance count",
        compute="_compute_aueov_sale_order_count",
        readonly=False,
    )

    abonnement_equipement_sale_subscription_count = fields.Integer(
        string="Equipement de maintenance count",
        compute="_compute_sale_subscription_count",
        readonly=False,
    )
    contrats_1_ids = fields.One2many(
        "sale.order", "abonnement_equipement_id", string="Contracts"
    )
    contrat_en_cours = fields.Char(
        related="contrats_1_ids.name", readonly=False, string="current_contract"
    )
    date_fin_contrat = fields.Date(
        related="contrats_1_ids.end_date",
        store=True,
        readonly=False,
        help="If set, the subscription will be marked as 'To renew' 1 month before the selected date and will be "
             "closed on that date.", string="Contract_end_date")
    contrat_type = fields.Char(related="contrats_1_ids.sale_order_template_id.name")
    client_utilisateur_id = fields.Many2one("res.partner", string="User client")
    proprietaire_id = fields.Many2one("res.partner", string="Owner")
    field_ixm1S = fields.Many2one("maintenance.version", string="Version")
    date_mise_jour = fields.Date(string="Date Updated")

    def _compute_aueov_sale_order_count(self):
        """
            Compute the number of Sale Orders associated with the current record.
        """
        self.aueov_sale_order_count = self.env["sale.order"].search_count(
            [("field_aueov_id", "in", self.ids)]
        )

    def action_view_sale_order(self):
        """
            Action to view Sale Orders related to the current record.
        """
        sale_order = self.env["sale.order"].search([("field_aueov_id", "in", self.ids)])
        return {
            "type": "ir.actions.act_window",
            "name": _("Sales"),
            "res_model": "sale.order",
            "view_mode": "tree,form",
            "domain": [("id", "in", sale_order.ids)],
        }

    def _compute_sale_subscription_count(self):
        """
            Compute the number of Sale Subscriptions associated with the current record.
        """
        # self.abonnement_equipement_sale_subscription_count = self.env['sale.order'].search_count(
        #     [('abonnement_equipement_id', 'in', self.ids), ('is_subscription', '=', True)]
        # )
        self.abonnement_equipement_sale_subscription_count = self.env[
            "sale.order"
        ].search_count(
            [("field_aueov_id", "in", self.ids), ("is_subscription", "=", True)]
        )
