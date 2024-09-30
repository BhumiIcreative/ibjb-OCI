# -*- coding: utf-8 -*-

{
    "name": "IBJB Studio",
    "version": "17.0.1.0.0",
    "category": "IBJB Studio",
    "summary": "IBJB Studio",
    "description": """
        Convert all studio customization to code""",
    "author": "Aktic software",
    "website": "http://www.aktivsoftware.com",
    "category": "Studio customization",
    "version": "17.0.1.0.0",
    "license": "LGPL-3",
    "depends": [
        "sale_subscription",
        "maintenance",
        "contacts",
        "account_followup",
        "delivery",
        "product",
        "purchase",
        "hr",
        'sale_management',
        # "sale"
        'helpdesk',
        'l10n_fr',
        'project',
        'stock',
        'crm',
        'account',
        'hr_attendance',
        'sale_stock',
        'stock_delivery',
        'purchase_stock',
        'product_expiry',
        'stock_barcode'
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/maintenance_security.xml",
        "data/action_add_fields.xml",
        "data/hr_mail_template.xml",
        "data/helpdesk_mail_template.xml",
        "views/maintenance_version_views.xml",
        "views/maintenance_etapes_pret_views.xml",
        "views/hr_employee_views.xml",
        "views/sale_order_views.xml",
        "views/account_partner_cat_views.xml",
        "views/naf_code_views.xml",
        "views/account_move_views.xml",
        "views/sale_subscription_views.xml",
        "views/maintenance_views.xml",
        "views/partner_view.xml",
        "views/purchase_views.xml",
        "views/res_company_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_type_views.xml",
        "views/helpdesk_source_views.xml",
        "views/ticket_gamme_views.xml",
        "views/res_users_views.xml",
        "views/hr_attendance_views.xml",
        "views/res_partner_views.xml",
        "views/stock_picking_views.xml",
        "views/product_pricelist_views.xml",
        "views/maintenance_request_views.xml",
        "report/product_pricelist_copy_1.xml",
        "report/transfer_report_1.xml",
        "report/transfer_report_2.xml",
        "report/transfer_report_3.xml",
        "report/report_paperformat.xml",
        "report/historique_maintenance_template.xml",
        "report/equipement_maintenance_template.xml",
        "report/maintenance_equipments_reports.xml",
        "report/report_purchase.xml",
        "report/ir_actions_report_templates.xml",
        "report/stock_paperformat.xml",
        "report/stock_picking_reports_actions.xml",
        "report/report_picking_copy_2.xml",
        "report/transfer_report_copy(1).xml",
        "report/picking_operations_copy_4.xml",
        "report/transfer_report_copy(2).xml",
        "report/acccount_move_report.xml",
        "report/account_move_facture_ce_intracommunautaire_template.xml",
        "report/account_move_facture_export_non_ce_template.xml",
        "report/sale_report_view.xml",
        "report/product_pricelist_priceoffer.xml",
        "report/product_pricelist_actions.xml",
        "report/account_move_facture_facto_cic_template.xml",
        "report/account_move_facture_franchise_de_tva_template.xml",
        "report/maintenance_request_report_template.xml",
        "report/maintenance_request_loan_equipment_removal_checklist_template.xml",
        "report/maintenance_request_report.xml",

    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
