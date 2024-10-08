# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


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
            ("DHL","DHL"),
            ("DPD","DPD"),
            ("TNT","TNT"),
            ("TSE","TSE"),
            ("ENLEVEMENT","ENLEVEMENT"),
            ("CHRONOPOST","CHRONOPOST"),
            ("CHRONOPOST INTERNATIONAL","CHRONOPOST INTERNATIONAL"),
            ("TNT INTERNATIONAL","TNT INTERNATIONAL"),
            ("Transporteur client / Customer carrier","Transporteur client / Customer carrier"),
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
