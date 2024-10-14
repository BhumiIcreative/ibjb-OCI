# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _
from odoo.addons.ibjb_studio import common


class Partner(models.Model):
    _inherit = "res.partner"

    customer_code = fields.Char(string="Code Tiers", copy=False) # x_studio_customer_code
    customer_contact = fields.Char(string="Contact", copy=False) # x_studio_customer_contact
    field_aD1p5 = fields.Selection(
        related="lang",
        string="Language",
        help=(
            "All emails and documents sent to this contact will be translated into this language."
        ),
        store=True,
        copy=False,
        readonly=False,
    ) # x_studio_field_aD1p5
    tva = fields.Char(string="TVA", copy=False) # x_studio_tva
    oci_contact_transporteur = fields.Selection(
        selection=[
            ("DHL", "DHL"),
            ("DPD", "DPD"),
            ("TNT", "TNT"),
            ("TSE", "TSE"),
            ("ENLEVEMENT", "ENLEVEMENT"),
            ("CHRONOPOST", "CHRONOPOST"),
            ("CHRONOPOST INTERNATIONAL", "CHRONOPOST INTERNATIONAL"),
            ("TNT INTERNATIONAL", "TNT INTERNATIONAL"),
            ("Transporteur client / Customer carrier", "Transporteur client / Customer carrier")
        ],
        copy=False,
        string="Transportor",
        store=True,
        tracking=True
    ) # x_studio_oci_contact_transporteur
    is_confidentiel = fields.Boolean("Confidentiel", copy=False) # x_studio_confidentiel
    is_suivi_1 = fields.Boolean("Suivi", copy=False) # x_studio_suivi_1
    is_sensible_2 = fields.Boolean("Sensible", copy=False) # x_studio_sensible_2
    proprietaire_maintenance_equipment_count = fields.Integer("Owner account",
                                                              compute='_compute_maintenance_count') # x_x_studio_proprietaire__maintenance_equipment_count
    maintenance_contact_maintenance_request_count = fields.Integer("Contact count",
                                                                   compute="_compute_maintenance_contact") # x_x_studio_maintenance_contact__maintenance_request_count
    name_product_supplierinfo_count = fields.Integer("Supplier price", compute='_compute_product_supplier_count') # x_name__product_supplierinfo_count
    oci_listprice_nomclient_product_pricelist_count = fields.Integer("Customer name account",
                                                                     compute='_compute_product_pricelist_count')  # x_x_studio_oci_listprice_nomclient__product_pricelist_count
    tva_msg_europe = fields.Char(
        "/!\ Il est obligatoire d'indiquer le numéro de TVA intracommunautaire client afin que la vente ne soit pas soumise à TVA.",
        copy=False)  # x_studio_tva_msg_europe
    country_group_ids_name = fields.Char("Continent", related='country_id.country_group_ids.name', copy=False,
                                         readonly=False)  # x_studio_country_group_ids_name
    field_BVkbJ_ids = fields.Many2many('ticket.gamme', 'res_partner_oci_ticket_gamme_rel', "Gamme",
                                       copy=False)  # x_studio_field_BVkbJ

    regroupement_id = fields.Many2one('regroupement.regroupement', string="Regroupement",
                                      ondelete='set null')  # x_studio_regroupement
    role_contact_id = fields.Many2one('contact.roles', ondelete='set null', string="Roles",
                                      copy=False)  # x_studio_role_contact
    center_interest_id = fields.Many2one("centre.interet", string="Center of interest", ondelete='set null',
                                         copy=False)  # x_studio_center_interest
    service_id = fields.Many2one("service.service", string="Service", ondelete='set null',
                                 copy=False)  # x_studio_code_affaire
    code_affaire_id = fields.Many2one("code.affaire", string="Code Affaire", ondelete='set null', copy=False)
    equipements_cmf_ids = fields.Many2many("equipement.cmf", "res_partner_equipement_cmf_rel", store=True,
                                           string="Equipements CMF", copy=False)  # x_studio_equipements_cmf
    field_LTJb8_ids = fields.Many2many("automates.client", "res_partner_automates_client_rel", store=True,
                                       string="Equipements IH", copy=False)  # x_studio_field_LTJb8
    equipements_bm_ids = fields.Many2many("automates.bm.clients", "res_partner_automates_bm_clients_rel",
                                          store=True,
                                          string="Equipements BM", copy=False)  # x_studio_equipements_bm
    facebook = fields.Char("Facebook", copy=False)  # x_studio_facebook
    linkedin = fields.Char("Linkedin", copy=False)  # x_studio_linkedin
    skype = fields.Char("Skype", copy=False)  # x_studio_skype
    precision_phone = fields.Char("Telephone details", copy=False)  # x_studio_precision_phone
    fax = fields.Char("Fax", copy=False)  # x_studio_fax
    customer_contact_fax = fields.Char("Fax", copy=False)  # x_studio_customer_contact_fax
    prestataire_maintenance = fields.Boolean(string=_("Prestataire"), copy=False)  # x_studio_prestataire_maintenance
    est_un_distributeur = fields.Boolean("Distributeur", copy=False)  # x_studio_est_un_distributeur
    code_naf_id = fields.Many2one('naf.code', "Code NAF", ondelete="set null")  # x_studio_code_naf
    categorie_comptable_id = fields.Many2one('account.partner.cat', ondelete='set null',
                                             string="Categorie Comptable")  # x_studio_categorie_comptable
    is_oci_contact_constt = fields.Boolean("Consentement total", copy=False)  # x_studio_oci_contact_constt
    is_oci_contact_consanonyme = fields.Boolean("Consentement anonyme uniquement",
                                                copy=False)  # x_studio_oci_contact_consanonyme
    is_oci_contact_pasconsentement = fields.Boolean("Pas de consentement", copy=False)
    chorus = fields.Char("Chorus", copy=False)  # x_studio_chorus
    oci_contact_commentaire = fields.Text("Commentaire", copy=False)  # x_studio_oci_contact_commentaire

    '''Compute the count of maintenance requests for each maintenance contact'''

    def _compute_maintenance_count(self):
        for rec in self:
            rec.proprietaire_maintenance_equipment_count = 0
            results = self.env['maintenance.equipment'].read_group(
                [('proprietaire_id', 'in', self.ids)],
                ['proprietaire_id'],
                ['proprietaire_id']
            )
            if results:
                equipment_count_dict = {res['proprietaire_id'][0]: res['proprietaire_id_count'] for res in
                                        results}
                rec.proprietaire_maintenance_equipment_count = equipment_count_dict.get(rec.id, 0)

    '''Compute the count of maintenance requests associated with each maintenance contact'''

    def _compute_maintenance_contact(self):
        for rec in self:
            rec.maintenance_contact_maintenance_request_count = 0
            results = self.env['maintenance.request'].read_group([('maintenance_contact_id', 'in', self.ids)],
                                                                 ['maintenance_contact_id'],
                                                                 ['maintenance_contact_id'])
            if results:
                contact_count_map = {
                    result['maintenance_contact_id'][0]: result['maintenance_contact_id_count']
                    for result in results
                }
                rec.maintenance_contact_maintenance_request_count = contact_count_map.get(rec.id, 0)

    '''Computes the count of supplier info related to each partner'''

    def _compute_product_supplier_count(self):
        for rec in self:
            rec.name_product_supplierinfo_count = 0
            results = self.env['product.supplierinfo'].read_group(
                [('partner_id', 'in', self.ids)],
                ['partner_id'],
                ['partner_id'])
            if results:
                vendor_count_map = {
                    result['partner_id'][0]: result['partner_id_count']
                    for result in results
                }
                rec.name_product_supplierinfo_count = vendor_count_map.get(rec.id, 0)

    '''Computes the count of product pricelists associated with a specific client'''

    def _compute_product_pricelist_count(self):
        for rec in self:
            rec.oci_listprice_nomclient_product_pricelist_count = 0
            results = self.env['product.pricelist'].read_group(
                [('listprice_nomclient_id', 'in', self.ids)],
                ['listprice_nomclient_id'],
                ['listprice_nomclient_id']
            )
            client_count_map = {
                result['listprice_nomclient_id'][0]: result['listprice_nomclient_id_count']
                for result in results
            }
            rec.oci_listprice_nomclient_product_pricelist_count = client_count_map.get(rec.id, 0)

    def Update_partner_studio_fields(self):
        print('\n\n\n\nUpdate_partner_studio_fields', self)
        """
        server action code to migrate partners studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_customer_code": "customer_code",
            "x_studio_customer_contact": "customer_contact",
            # 'x_studio_field_aD1p5': 'field_aD1p5', # No need to migarte this fields as it is related to base field lang
            "x_studio_tva": "tva",
        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
