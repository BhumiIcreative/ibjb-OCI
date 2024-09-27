# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.addons.ibjb_studio import common


class ProductTemplate(models.Model):
    _inherit = "product.pricelist"

    listprice_referencepdf = fields.Char(string="Quality document ref")
    offre_de_prix_annee = fields.Char(string="Year of offer")
    offre_de_prix = fields.Boolean(string="Price offer")
    listprice_nomclient_id = fields.Many2one('res.partner', string="Customer Name")
    pricelist_alintentionde = fields.Char(string="To the attention of")
    istprice_codetiers = fields.Char(string="Code tiers",related="listprice_nomclient_id.customer_code")
    pricelist_orderref = fields.Char(string="Offer reference")
    datelifeend = fields.Date(string="End date")
    pricelist_faitle = fields.Char(string="Made at")
    pricelist_faita = fields.Date(string="Do it")
    is_listprice_france = fields.Boolean(string="Price offer France")
    listprice_francetext = fields.Text(string="Mandatory text FR 2")
    is_listprice_horsfrance = fields.Boolean(string="Price offer outside France")
    listprice_horsfrancetext = fields.Text(string="Mandatory text HFR 2")
    pricelist_conditionspaiement = fields.Char(string="Payment terms",related="listprice_nomclient_id.property_payment_term_id.display_name")
    listprice_horsfrancetext2 = fields.Text(string="Mandatory text HFR 1")
    pricelist_comeventuel = fields.Text(string="Possible comment")
    listprice_francetext2 = fields.Text(string="Mandatory text FR 1")

class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    field_MqbX7 = fields.Char(
        related="product_tmpl_id.default_code",
        string="Product reference",
        copy=False,
        store=True,
        readonly=False,
    ) # No need to migarte this fields as it is related field

    oci_pricelist_coms = fields.Text(
        string="New Multiline Text",
        copy=False,
        store=True,
    )

    saleorder_pricelist_productdate = fields.Char(
        string="New Text",
        copy=False,
        store=True,
    )

    def Update_product_pricelist_item_studio_fields(self):
        """
        server action code to migrate Product pricelist items studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_oci_pricelist_coms": "oci_pricelist_coms",
            "x_studio_x_studio_saleorder_pricelist_productdate": "saleorder_pricelist_productdate",
        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)