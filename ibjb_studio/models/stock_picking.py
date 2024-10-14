# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields,api
from odoo.addons.ibjb_studio import common


class ResCompany(models.Model):
    _inherit = 'stock.picking'

    is_expdition_bloque = fields.Boolean(_('Shipping blocked'))
    client_reference = fields.Char(_('Customer Reference'), related='sale_id.client_order_ref')
    product_reference = fields.Char(_('Product Reference'), related='sale_id.client_order_ref')
    date_commande = fields.Datetime(_('order date'), related='sale_id.date_order')
    abonnementsurbl = fields.Char(_('Subscription'),
                                  related='sale_id.subscription_id.display_name')
    bl_abobdc = fields.Char(_('Linked subscription'),
                            related='sale_id.subscription_id.display_name')
    bl_btverif_id = fields.Many2one('hr.employee', _('BT verified by'))
    bl_commentairetxt = fields.Text(_('Order comment'))
    bl_conditionvente = fields.Text(_('Conditions of sale'))
    bl_codetiers = fields.Char(_('Third party code BL'),related='sale_id.oci_saleorder_codetiers')
    br_codetiers = fields.Char(_('BR third party code'),related="purchase_id.oci_achat_devis_codetiers")
    bl_dimension = fields.Char(_('Dimension'))
    bl_poids = fields.Char(_('Weight'))
    bl_port = fields.Char(_('Port'))
    bl_prepareele_1 = fields.Date(_('Prepared on'))
    bl_prepareepar_id = fields.Many2one('hr.employee', _('Prepared by'))
    bl_verifieele = fields.Date(_('Checked on'))
    bl_verifieepar = fields.Many2one('hr.employee', _('Verified by'))
    is_blbr_imprimer_ouinon = fields.Boolean(_('BL Printed'))
    blbr_analyse = fields.Char(_('Analysis sheet'))
    blbr_crgs = fields.Char(_('N°CRGS'))
    blbr_faita = fields.Char(_('Made at'))
    blbr_faitle = fields.Date(_('Do it'))
    blbr_lotcrg = fields.Char(_('Corrected batch'))
    blbr_qtecrg = fields.Char(_('Corrected quantity'))
    blbr_remarque = fields.Text(_('Noticed'))
    inventory_settingociadmin = fields.Selection(string='Customer language', related='partner_id.lang')
    total_weight = fields.Float(_('Total Weight'))
    bl_transporteur = fields.Selection([
        ("chronopost", "Chronopost"),
        ("chronopost_international", "Chronopost International"),
        ("dhl", "DHL"),
        ("dpd", "DPD"),
        ("tnt", "TNT"),
        ("tnt_international", "TNT International"),
        ("tse", "TSE"),
        ("enlevement", "Kidnapping")
    ], _("Carrier"))
    bl_dateexpetsht = fields.Datetime(_('Desired shipping date'),readonly=True)


    @api.model
    def update_stock_picking_studio_fields(self):
        print('\n\n\nmethod called')

        migration_fields = {
            "x_studio_expdition_bloque": "is_expdition_bloque",
            "x_studio_field_LQ1TX": "client_reference",
            "x_studio_field_itTx0": "product_reference",
            "x_studio_field_n2pvH": "date_commande",
            "x_studio_oci_abonnementsurbl": "abonnementsurbl",
            # "x_studio_oci_bl_abobdc": "bl_abobdc",
            "x_studio_oci_bl_btverif": "bl_btverif_id",
            "x_studio_oci_bl_codetiers": "bl_codetiers",
            "x_studio_oci_bl_commentairetxt": "bl_commentairetxt",
            "x_studio_oci_bl_conditionvente": "bl_conditionvente",
            "x_studio_oci_bl_dateexpetsht": "bl_dateexpetsht",
            "x_studio_oci_bl_dimension": "bl_dimension",
            "x_studio_oci_bl_poids": "bl_poids",
            "x_studio_oci_bl_port": "bl_port",
            "x_studio_oci_bl_prepareele_1": "bl_prepareele_1",
            "x_studio_oci_bl_prepareepar": "bl_prepareepar_id",
            "x_studio_oci_bl_transporteur": "bl_transporteur",
            "x_studio_oci_bl_verifieele": "bl_verifieele",
            "x_studio_oci_bl_verifieepar": "bl_verifieepar",
            "x_studio_oci_blbr__imprimer_ouinon": "is_blbr_imprimer_ouinon",
            "x_studio_oci_blbr_analyse": "blbr_analyse",
            "x_studio_oci_blbr_crgs": "blbr_crgs",
            "x_studio_oci_blbr_faita": "blbr_faita",
            "x_studio_oci_blbr_faitle": "blbr_faitle",
            "x_studio_oci_blbr_lotcrg": "blbr_lotcrg",
            "x_studio_oci_blbr_qtecrg": "blbr_qtecrg",
            "x_studio_oci_blbr_remarque": "blbr_remarque",
            "x_studio_oci_br_codetiers": "br_codetiers",
            "x_studio_oci_inventory_settingociadmin": "inventory_settingociadmin",
            "x_studio_total_weight": "total_weight",
        }

        stock_pickings = self.search([])
        print('\n\n\nstock_pickings', stock_pickings)  # Fetch all picking records
        for rec in stock_pickings:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
