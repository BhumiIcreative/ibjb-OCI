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
    "license": "AGPL-3",
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
        'sale_management'
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/maintenance_security.xml",
        "data/action_add_fields.xml",
        "views/maintenance_version_views.xml",
        "views/maintenance_etapes_pret_views.xml",
        "views/hr_employee_views.xml",
        "views/sale_order_views.xml",
        "views/maintenance_views.xml",
        "views/account_move_views.xml",
        "views/account_partner_cat_views.xml",
        "views/naf_code_views.xml",
        "views/sale_subscription_views.xml",
        "views/partner_view.xml",
        "views/purchase_views.xml",
        "views/sale_order_views.xml",
        "report/report_paperformat.xml",
        "report/maintenance_reports.xml",
        "report/historique_maintenance_template.xml",
        "report/equipement_maintenance_template.xml",
        "report/report_purchase.xml",
        "report/ir_actions_report_templates.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
