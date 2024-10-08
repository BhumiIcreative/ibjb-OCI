# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.addons.ibjb_studio import common


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
        "sale.order", "abonnement_equipement_id",
        string="Contracts",
    )
    contrat_en_cours = fields.Char(
        related="contrats_1_ids.name",
        readonly=False,
        store=True,
        string="current_contract",
        tracking=True
    )
    date_fin_contrat = fields.Date(
        related="contrats_1_ids.end_date",
        store=True,
        readonly=False,
        tracking=True,
        help="If set, the subscription will be marked as 'To renew' 1 month before the selected date and will be "
             "closed on that date.", string="Contract_end_date")
    contrat_type = fields.Char(
        related="contrats_1_ids.sale_order_template_id.name",
        string="Contrat type",
        store=True,
        readonly=False,
    )
    client_utilisateur_id = fields.Many2one("res.partner", string="User client")
    proprietaire_id = fields.Many2one("res.partner", string="Owner")
    field_ixm1S_id = fields.Many2one("maintenance.version", string="Version")
    date_mise_jour = fields.Date(string="Date Updated")
    date_de_vente = fields.Date(string="Order date")

    def _compute_aueov_sale_order_count(self):
        """
            Compute the number of Sale Orders associated with the current record.
        """
        self.aueov_sale_order_count = self.env["sale.order"].search_count(
            [("field_aueov_id", "in", self.ids)]
        )

    def _compute_sale_subscription_count(self):
        """
            Compute the number of Sale Subscriptions associated with the current record.
        """
        self.abonnement_equipement_sale_subscription_count = self.env['sale.order'].search_count(
            [('abonnement_equipement_id', 'in', self.ids), ('is_subscription', '=', True)]
        )

    def Update_maintenance_equipment_studio_fields(self):
        """
            server action code to migrate Maintenance Equipment studio fields data to custom fields.
        """
        migration_fields = {
            "x_x_studio_field_aueov__sale_order_count": "aueov_sale_order_count",
            "x_x_studio_abonnement_equipement__sale_subscription_count": "abonnement_equipement_sale_subscription_count",
            "x_studio_contrat_en_cours": "contrat_en_cours",
            "x_studio_date_fin_contrat": "date_fin_contrat",
            "x_studio_contrat_type": "contrat_type",
            # "x_studio_contrats_1": "contrats_1_ids",
            "x_studio_client_utilisateur": "client_utilisateur_id",
            "x_studio_proprietaire": "proprietaire_id",
            "x_studio_field_ixm1S": "field_ixm1S_id",
            "x_studio_date_mise_jour": "date_mise_jour",
            "x_studio_date_de_vente": "date_de_vente",
        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
