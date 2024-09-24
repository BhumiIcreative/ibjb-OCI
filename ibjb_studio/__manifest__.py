# -*- coding: utf-8 -*-

{
    "name": "IBJB Studio",
    "version": "17.0.1.0.0",
    "category": "IBJB Studio",
    "summary": "IBJB Studio",
    "description": """
        IBJB Studio
    """,
    "author": "",
    "website": "",
    "license": "OPL-1",
    "depends": ['sale_management', 'hr', 'maintenance', 'sale_subscription'],
    "data": [
        'security/ir.model.access.csv',
        'reports/report_paperformat.xml',
        'reports/maintenance_reports.xml',
        'reports/historique_maintenance_template.xml',
        'reports/equipement_maintenance_template.xml',
        'views/maintenance_version_views.xml',
        'views/maintenance_etapes_pret_views.xml',
        'views/hr_employee_views.xml',
        'views/maintenance_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
