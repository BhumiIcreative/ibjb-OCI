# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.addons.ibjb_studio import common

# logger = logging.getLogger(__name_)


# from v12.enterprise.pos_blackbox_be.models.pos_blackbox_be import product_template


class SaleOrder(models.Model):
    _inherit = "sale.order"

    abonnement_equipement_id = fields.Many2one(
        "maintenance.equipment",
        string="Maintenance Equipement",
        ondelete="set null",
        copy=False,
    )  # sale_subscription field

    # No need to migarte below fields as they are all related field
    customer_vat = fields.Char(
        related="partner_id.tva",
        string="Customer TVA",
        readonly=True,
        copy=False,
        store=True,
    )
    oci_saleorder_codetiers = fields.Char(
        related="partner_id.customer_code",
        string="Code tiers",
        readonly=True,
        copy=False,
        store=True,
    )
    oci_vente_langcustomer = fields.Selection(
        related="partner_id.lang",
        string="Customer language",
        help=(
            "All emails and documents sent to this contact will be translated into this language."
        ),
        store=True,
        copy=False,
        readonly=True,
    )

    field_aueov_id = fields.Many2one(
        "maintenance.equipment", string="Equipement de maintenance"
    )

    oci_bdc_dateexpsht = fields.Date(
        string="Desired shipping date",
        store=True,
        copy=False,
    )

    oci_sale_priceliste_enddate = fields.Date(
        related="pricelist_id.datelifeend",
        string="End of validity of price list",
        store=True,
        copy=False,
    )

    saleorder_order_carrier = fields.Selection(
        related="partner_id.oci_contact_transporteur",
        string="Transportor Carrier",
        copy=False,
        readonly=True,
    )

    oci_bdc_transporteur = fields.Selection(
        selection=[
            ("DHL", "DHL"),
            ("DPD", "DPD"),
            ("TNT", "TNT"),
            ("TSE", "TSE"),
            ("ENLEVEMENT", "ENLEVEMENT"),
            ("CHRONOPOST", "CHRONOPOST"),
            ("CHRONOPOST INTERNATIONAL", "CHRONOPOST INTERNATIONAL"),
            ("TNT INTERNATIONAL", "TNT INTERNATIONAL"),
            ("Transporteur client / Customer carrier", "Transporteur client / Customer carrier"),
        ],
        copy=False,
        string="Transportor",
        store=True,
        tracking=True,
    )

    oci_chplie_customercomment1 = fields.Html(
        related="partner_id.comment",
        string="Internal note",
        copy=False,
        readonly=True,
        store=True,
    )

    purchase_order_reference = fields.Char(
        string="Order reference",
        copy=False,
        store=True,
    )

    tva_msg_europe = fields.Char(
        copy=False,
        store=True,
    )

    @api.model
    def update_studio_fields(self):
        print('\n\n\n\nupdate_sale_studio_fields', self)
        """
        schedule action code to migrate sale studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_customer_tva": "customer_vat",
            "x_studio_oci_saleorder_codetiers":"oci_saleorder_codetiers",
            "x_studio_oci_vente_langcustomer":"oci_vente_langcustomer",
            "x_studio_abonnement_equipement":"abonnement_equipement_id",
            "x_studio_purchase_order_reference":"purchase_order_reference",
            "x_studio_oci_chplie_customercomment1":"oci_chplie_customercomment1",
            "x_studio_oci_bdc_transporteur":"oci_bdc_transporteur",
            "x_studio_saleorder_order_carrier":"saleorder_order_carrier",
            "x_studio_oci_sale_priceliste_enddate":"oci_sale_priceliste_enddate",
            "x_studio_oci_bdc_dateexpsht":"oci_bdc_dateexpsht",
            "x_studio_field_aueov":"field_aueov_id",
            "x_studio_tva_msg_europe":"tva_msg_europe"
        }
        sale_orders = self.search([])  # Fetch all sale  records
        print('\n\n\n\nsale_orders',sale_orders)
        for rec in sale_orders:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)

