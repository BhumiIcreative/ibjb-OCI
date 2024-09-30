# -*- coding: utf-8 -*-
from odoo import fields, models


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
