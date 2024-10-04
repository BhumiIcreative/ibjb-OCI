# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields


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
