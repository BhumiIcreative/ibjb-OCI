# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.addons.ibjb_studio import common


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    ad_client_2 = fields.Binary(
        string="File 2",
        copy=False,
        store=True,
    )

    ad_client_2_filename = fields.Char(
        string="Filename for x_studio_ad_client_2",
        copy=False,
        store=True,
    )

    ad_client_3 = fields.Binary(
        string="File 3",
        copy=False,
        store=True,
    )

    ad_client_complte = fields.Boolean(
        string="Customer AD completed",
        copy=False,
        store=True,
    )

    ad_client_complte_1 = fields.Boolean(
        string="Customer AD completed 1",
        copy=False,
        store=True,
    )

    ad_client_vierge_1 = fields.Binary(
        string="File 4",
        copy=False,
        store=True,
    )

    ad_client_vierge_pour_automate_client_aller = fields.Boolean(
        string="Blank Client AD for Go Client PLC",
        copy=False,
        store=True,
    )

    ad_client_vierge_pour_automate_prt_retour = fields.Boolean(
        string="Blank client AD for automaton ready return",
        copy=False,
        store=True,
    )

    ad_ibjb_1 = fields.Binary(
        string="File 5",
        copy=False,
        store=True,
    )

    ad_ibjb_3 = fields.Binary(
        string="File 6",
        copy=False,
        store=True,
    )

    ad_ibjb_4 = fields.Binary(
        string="File 7",
        copy=False,
        store=True,
    )

    ad_ibjb_completee = fields.Boolean(
        string="AD IBJB completed",
        copy=False,
        store=True,
    )

    ad_ibjb_complte = fields.Boolean(
        string="AD IBJB completed 2",
        copy=False,
        store=True,
    )

    bl_automate = fields.Boolean(
        string="BL automate",
        copy=False,
        store=True,
    )

    bl_automate_client = fields.Boolean(
        string="BL automate 2",
        copy=False,
        store=True,
    )

    bl_automate_fichier = fields.Binary(
        string="File 8",
        copy=False,
        store=True,
    )

    bl_fichier_client = fields.Binary(
        string="File 9",
        copy=False,
        store=True,
    )

    bt_pour_transport_automate_prt_retour = fields.Boolean(
        string="BT for transport, automatic return ready",
        copy=False,
        store=True,
    )

    bt_tp_cli_aller = fields.Binary(
        string="File 10",
        copy=False,
        store=True,
    )

    bt_transp_pret_4 = fields.Binary(
        string="File 11",
        copy=False,
        store=True,
    )

    bt_transport_automate_client_aller = fields.Boolean(
        string="BT transport customer automaton go",
        copy=False,
        store=True,
    )

    carton_de_lautomate_de_prt_avec_les_tiquettes_hautbas = fields.Boolean(
        string="Cardboard machine ready with top/bottom labels",
        copy=False,
        store=True,
    )

    carton_dorigine_ou_dfaut_carton_de_lautomate_de_prt = fields.Boolean(
        string="Original box or failing that box from the loan machine",
        copy=False,
        store=True,
    )

    carton_origine_hautbas_ou_carton_automate_prt_hautbas = fields.Boolean(
        string="Top/bottom original box or top/bottom ready machine box",
        copy=False,
        store=True,
    )

    conclusion_et_conseils_au_client = fields.Text(
        string="Conclusion and advice to the client",
        copy=False,
        store=True,
    )

    date_ouverture = fields.Date(
        string="Opening date",
        copy=False,
        store=True,
    )

    demande_de_pret_id = fields.Many2one(
        'maintenance.request',
        string="Loan request",
        ondelete="set null",
        store=True,
    )

    description_maintenance = fields.Text(
        string="Description",
        copy=False,
        store=True,
    )

    etape_du_prt_id = fields.Many2one(
        'maintenance.etapes.pret',
        string="Loan stage",
        copy=False,
        store=True,
    )

    fiche_pret_1 = fields.Binary(
        string="File 12",
        copy=False,
        store=True,
    )

    fiche_pret_4 = fields.Binary(
        string="File 13",
        copy=False,
        store=True,
    )

    fiche_prt_complte_sur_partie_aller = fields.Boolean(
        string="Loan form completed on the “go” part",
        copy=False,
        store=True,
    )

    fiche_prt_complte_sur_partie_retour = fields.Boolean(
        string="Loan form completed on return portion",
        copy=False,
        store=True,
    )

    fiche_prt_contre_signe = fields.Binary(
        string="Countersigned loan form",
        copy=False,
        store=True,
    )

    fiche_prt_contre_signe_sur_partie_retour = fields.Binary(
        string="Countersigned loan form on “return” part",
        copy=False,
        store=True,
    )

    fiche_transp_2 = fields.Binary(
        string="File 14",
        copy=False,
        store=True,
    )

    fiche_transp_3 = fields.Binary(
        string="File 15",
        copy=False,
        store=True,
    )

    fiche_transp_vierge_1 = fields.Binary(
        string="File 16",
        copy=False,
        store=True,
    )

    fiche_transport_complte_sur_partie_aller = fields.Boolean(
        string="Transport form completed on the “outbound” part",
        copy=False,
        store=True,
    )

    fiche_transport_complte_sur_partie_retour = fields.Boolean(
        string="Transport form completed on the “return” section",
        copy=False,
        store=True,
    )

    fiche_transport_contre_signe = fields.Binary(
        string="Countersigned transport form outbound part",
        copy=False,
        store=True,
    )

    fiche_transport_contresignee_retour = fields.Binary(
        string="Countersigned transport form on return part",
        copy=False,
        store=True,
    )

    fiche_transport_vierge = fields.Boolean(
        string="Blank transport sheet",
        copy=False,
        store=True,
    )

    fichier = fields.Binary(
        string="File 17",
        copy=False,
        store=True,
    )

    field_wExXP = fields.Binary(
        string="New File",
        copy=False,
        store=True,
    )

    flacons_de_transport = fields.Boolean(
        string="Transport bottles",
        copy=False,
        store=True,
    )

    flacons_de_transport_1 = fields.Boolean(
        string="Transport bottles 1",
        copy=False,
        store=True,
    )

    flacons_de_transport_2 = fields.Boolean(
        string="Transport bottles 2",
        copy=False,
        store=True,
    )

    flacons_de_transport_3 = fields.Boolean(
        string="Transport bottles 3",
        copy=False,
        store=True,
    )

    haut_bas_fragile_sur_carton = fields.Boolean(
        string="Top/bottom/fragile on cardboard",
        copy=False,
        store=True,
    )

    maintenance_contact_id = fields.Many2one(
        'res.partner',
        string='Customer',
        ondelete="set null",
        copy=False,
        store=True,
    )

    maintenance_contact_interlocuteur_id = fields.Many2one(
        'res.partner',
        string="Interlocutor",
        ondelete="set null",
        copy=False,
        store=True,
    )

    maintenance_solution = fields.Text(
        string="Tasks and measures carried out",
        copy=False,
        store=True,
    )

    manuel_papier = fields.Boolean(
        string="Paper manual",
        copy=False,
        store=True,
    )

    oci_maint_date_enlev_client = fields.Date(
        string="Customer collection date",
        copy=False,
        store=True,
    )

    oci_maint_date_enlv_pret = fields.Date(
        string="Pick-up date ready",
        copy=False,
        store=True,
    )

    oci_maint_date_envoi_client = fields.Date(
        string="Customer dispatch date",
        copy=False,
        store=True,
    )

    oci_maint_date_envoi_pret = fields.Date(
        string="Ready shipping date",
        copy=False,
        store=True,
    )

    oci_maintenance_liee_id = fields.Many2one(
        'maintenance.request',
        string="Related maintenance",
        ondelete="set null",
        copy=False,
        store=True,
    )

    pret_de_matriel = fields.Boolean(
        string="Requires an equipment loan?",
        copy=False,
        store=True,
    )

    ri_complt_et_sign = fields.Boolean(
        string="RI completed and signed",
        copy=False,
        store=True,
    )

    ri_signe_3 = fields.Binary(
        string="File 18",
        copy=False,
        store=True,
    )

    ri_signe_3_filename = fields.Char(
        string="Filename for x_studio_ri_signe_3",
        copy=False,
        store=True,
    )

    sous_traitant_id = fields.Many2one(
        'res.partner',
        string="Subcontractor",
        ondelete="set null",
        copy=False,
        store=True,
    )

    suivi_de_prt = fields.Boolean(
        string="Loan monitoring?",
        copy=False,
        store=True,
    )

    systme_conforme_aux_spcifications_fabricant = fields.Boolean(
        string="System complies with manufacturer specifications",
        copy=False,
        store=True,
    )

    fiche_transp_vierge_1_filename = fields.Char(
        string="Filename for x_studio_fiche_transp_vierge_1",
        copy=False,
        store=True,
    )

    def Update_maintenance_request_studio_fields(self):
        """
        server action code to migrate Product pricelist items studio fields data to custom fields.
        """
        migration_fields = {
            'x_studio_ad_client_2': 'ad_client_2',
            "x_studio_ad_client_2_filename": "ad_client_2_filename",
            "x_studio_ad_client_3": "ad_client_3",
            "x_studio_ad_client_complte": "ad_client_complte",
            "x_studio_ad_client_complte_1": "ad_client_complte_1",
            "x_studio_ad_client_vierge_1": "ad_client_vierge_1",
            "x_studio_ad_client_vierge_pour_automate_client_aller": "ad_client_vierge_pour_automate_client_aller",
            "x_studio_ad_client_vierge_pour_automate_prt_retour": "ad_client_vierge_pour_automate_prt_retour",
            "x_studio_ad_ibjb_1": "ad_ibjb_1",
            "x_studio_ad_ibjb_3": "ad_ibjb_3",
            "x_studio_ad_ibjb_4": "ad_ibjb_4",
            "x_studio_ad_ibjb_completee": "ad_ibjb_completee",
            "x_studio_ad_ibjb_complte": "ad_ibjb_complte",
            "x_studio_bl_automate": "bl_automate",
            "x_studio_bl_automate_client": "bl_automate_client",
            "x_studio_bl_automate_fichier": "bl_automate_fichier",
            "x_studio_bl_fichier_client": "bl_fichier_client",
            "x_studio_bt_pour_transport_automate_prt_retour": "bt_pour_transport_automate_prt_retour",
            "x_studio_bt_tp_cli_aller": "bt_tp_cli_aller",
            "x_studio_bt_transp_pret_4": "bt_transp_pret_4",
            "x_studio_bt_transport_automate_client_aller": "bt_transport_automate_client_aller",
            "x_studio_carton_de_lautomate_de_prt_avec_les_tiquettes_hautbas": "carton_de_lautomate_de_prt_avec_les_tiquettes_hautbas",
            "x_studio_carton_dorigine_ou_dfaut_carton_de_lautomate_de_prt": "carton_dorigine_ou_dfaut_carton_de_lautomate_de_prt",
            "x_studio_carton_origine_hautbas_ou_carton_automate_prt_hautbas": "carton_origine_hautbas_ou_carton_automate_prt_hautbas",
            "x_studio_conclusion_et_conseils_au_client": "conclusion_et_conseils_au_client",
            "x_studio_date_ouverture": "date_ouverture",
            # "x_studio_demande_de_pret": "demande_de_pret_id",
            "x_studio_description_maintenance": "description_maintenance",
            # "x_studio_etape_du_prt": "etape_du_prt_id",
            "x_studio_fiche_pret_1": "fiche_pret_1",
            "x_studio_fiche_pret_4": "fiche_pret_4",
            "x_studio_fiche_prt_complte_sur_partie_aller_": "fiche_prt_complte_sur_partie_aller",
            "x_studio_fiche_prt_complte_sur_partie_retour": "fiche_prt_complte_sur_partie_retour",
            "x_studio_fiche_prt_contre_signe": "fiche_prt_contre_signe",
            "x_studio_fiche_prt_contre_signe_sur_partie_retour": "fiche_prt_contre_signe_sur_partie_retour",
            "x_studio_fiche_transp_2": "fiche_transp_2",
            "x_studio_fiche_transp_3": "fiche_transp_3",
            "x_studio_fiche_transp_vierge_1": "fiche_transp_vierge_1",
            "x_studio_fiche_transport_complte_sur_partie_aller_": "fiche_transport_complte_sur_partie_aller",
            "x_studio_fiche_transport_complte_sur_partie_retour_": "fiche_transport_complte_sur_partie_retour",
            "x_studio_fiche_transport_contre_signe": "fiche_transport_contre_signe",
            "x_studio_fiche_transport_contresignee_retour": "fiche_transport_contresignee_retour",
            "x_studio_fiche_transport_vierge": "fiche_transport_vierge",
            "x_studio_fichier": "fichier",
            "x_studio_field_wExXP": "field_wExXP",
            "x_studio_flacons_de_transport": "flacons_de_transport",
            "x_studio_flacons_de_transport_1": "flacons_de_transport_1",
            "x_studio_flacons_de_transport_2": "flacons_de_transport_2",
            "x_studio_flacons_de_transport_3": "flacons_de_transport_3",
            "x_studio_haut_bas_fragile_sur_carton": "haut_bas_fragile_sur_carton",
            # "x_studio_maintenance_contact": "maintenance_contact",
            # "x_studio_maintenance_contact_interlocuteur": "maintenance_contact_interlocuteur_id",
            "x_studio_maintenance_solution": "maintenance_solution",
            "x_studio_manuel_papier": "manuel_papier",
            "x_studio_oci_maint_date_enlev_client": "oci_maint_date_enlev_client",
            "x_studio_oci_maint_date_enlv_pret": "oci_maint_date_enlv_pret",
            "x_studio_oci_maint_date_envoi_client": "oci_maint_date_envoi_client",
            "x_studio_oci_maint_date_envoi_pret": "oci_maint_date_envoi_pret",
            # "x_studio_oci_maintenance_liee": "oci_maintenance_liee_id",
            "x_studio_pret_de_matriel_": "pret_de_matriel",
            "x_studio_ri_complt_et_sign": "ri_complt_et_sign",
            "x_studio_ri_signe_3": "ri_signe_3",
            "x_studio_ri_signe_3_filename": "ri_signe_3_filename",
            # "x_studio_sous_traitant": "sous_traitant_id",
            "x_studio_suivi_de_prt_": "suivi_de_prt",
            "x_studio_systme_conforme_aux_spcifications_fabricant": "systme_conforme_aux_spcifications_fabricant",
            "x_studio_fiche_transp_vierge_1_filename": "fiche_transp_vierge_1_filename",
        }

        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
