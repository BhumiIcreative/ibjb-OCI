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
        "product",
        'sale_management',
        'helpdesk',
        'l10n_fr',
        'project',
        'stock',
        'crm',
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
        "views/maintenance_views.xml",
        "views/account_partner_cat_views.xml",
        "views/naf_code_views.xml",
        "views/account_move_views.xml",
        "views/sale_subscription_views.xml",
        "views/partner_view.xml",
        "views/purchase_views.xml",
        "views/sale_order_views.xml",
        "views/res_company_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_type_views.xml",
        "views/helpdesk_source_views.xml",
        "views/ticket_gamme_views.xml",
        "views/res_users_views.xml",
        "views/hr_attendance_views.xml",
        "views/res_partner_views.xml",
        "views/stock_picking_views.xml",

        "report/report_paperformat.xml",
        "report/maintenance_reports.xml",
        "report/historique_maintenance_template.xml",
        "report/equipement_maintenance_template.xml",
        "report/report_purchase.xml",
        "report/ir_actions_report_templates.xml",
        "report/stock_paperformat.xml",
        "report/report_picking_copy_2.xml",
        "report/transfer_report_copy(1).xml",
        "report/picking_operations_copy_4.xml",
        "report/transfer_report_copy(2).xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
