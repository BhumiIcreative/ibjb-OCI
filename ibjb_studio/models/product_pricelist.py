# -*- coding: utf-8 -*-

from odoo import fields, models,api
from odoo.addons.ibjb_studio import common


class ProductTemplate(models.Model):
    _inherit = "product.pricelist"

    listprice_referencepdf = fields.Char(string="Quality document ref")
    offre_de_prix_annee = fields.Char(string="Year of offer")
    offre_de_prix = fields.Boolean(string="Price offer")
    listprice_nomclient_id = fields.Many2one('res.partner', string="Customer Name")
    pricelist_alintentionde = fields.Char(string="To the attention of")
    istprice_codetiers = fields.Char(string="Code tiers", related="listprice_nomclient_id.customer_code")
    pricelist_orderref = fields.Char(string="Offer reference")
    datelifeend = fields.Date(string="End date")
    pricelist_faitle = fields.Char(string="Made at")
    pricelist_faita = fields.Date(string="Do it")
    is_listprice_france = fields.Boolean(string="Price offer France")
    listprice_francetext = fields.Text(string="Mandatory text FR 2")
    is_listprice_horsfrance = fields.Boolean(string="Price offer outside France")
    listprice_horsfrancetext = fields.Text(string="Mandatory text HFR 2")
    pricelist_conditionspaiement = fields.Char(string="Payment terms",
                                               related="listprice_nomclient_id.property_payment_term_id.display_name")
    listprice_horsfrancetext2 = fields.Text(string="Mandatory text HFR 1")
    pricelist_comeventuel = fields.Text(string="Possible comment")
    listprice_francetext2 = fields.Text(string="Mandatory text FR 1")
    notes = fields.Text(string="Notes")
    date_life_start = fields.Date(string="Start date")
    address = fields.Char(
        string="Address",
        related="listprice_nomclient_id.contact_address",
        readonly=True,
        store=False,
    )
    textbul = fields.Char(string="Info")
    warming = fields.Char(string="Warming")

    @api.model
    def update_pricelist_studio_fields(self):
        """
        schedule action code to migrate sale studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_notes": "notes",
            "x_studio_offre_de_prix": "offer_de_prix",
            "x_studio_oci_datelifeend": "datelifeend",
            "x_studio_oci_datelifestart": "date_life_start",
            "x_studio_oci_listprice_nomclient": "listprice_nomclient_id",
            "x_studio_field_i1oej": "address",
            "x_studio_oci_listprice_codetiers": "istprice_codetiers",
            "x_studio_oci_pricelist_faitle": "pricelist_faitle",
            "x_studio_oci_pricelist_faita": "pricelist_faita",
            "x_studio_oci_textbul": "textbul",
            "x_studio_x_studio_x_studio_offre_de_prix_annee": "offre_de_prix_annee",
            "x_studio_oci_listprice_referencepdf": "listprice_referencepdf",
            "x_studio_oci_listprice_france": "is_listprice_france",
            "x_studio_oci_listprice_francetext": "listprice_francetext",
            "x_studio_oci_listprice_horsfrance": "is_listprice_horsfrance",
            "x_studio_oci_listprice_horsfrancetext": "listprice_horsfrancetext",
            "x_studio_field_4jjJH": "warming",
            "x_studio_oci_pricelist_conditionspaiement": "pricelist_conditionspaiement",
            "x_studio_oci_pricelist_alintentionde": "pricelist_alintentionde",
            "x_studio_oci_pricelist_comeventuel": "pricelist_comeventuel",
            "x_studio_oci_pricelist_orderref": "pricelist_orderref",
            "x_studio_x_studio_oci_listprice_francetext2": "listprice_francetext2",
            "x_studio_x_studio_oci_listprice_horsfrancetext2": "listprice_horsfrancetext2",
        }
        pricelist_orders = self.search([])  # Fetch all sale  records
        for rec in pricelist_orders:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)

