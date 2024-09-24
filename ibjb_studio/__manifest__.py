# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "ibjb studio",
    'summary': "ibjb studio",
    'description': "ibjb studio",
    'author': "Aktiv Software",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'account',
    'version': '17.0.1.0.0',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts','helpdesk', 'l10n_fr','project','stock','crm','maintenance','hr','hr_attendance','sale_stock','sale_subscription','stock_delivery','purchase_stock','product_expiry','stock_barcode'],
    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "data/hr_mail_template.xml",
        "data/helpdesk_mail_template.xml",
        "report/stock_paperformat.xml",
        "report/report_picking_copy_2.xml",
        "report/transfer_report_copy(1).xml",
        "report/picking_operations_copy_4.xml",
        "report/transfer_report_copy(2).xml",
        "views/res_company_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_type_views.xml",
        "views/helpdesk_source_views.xml",
        "views/ticket_gamme_views.xml",
        "views/res_users_views.xml",
        "views/hr_attendance_views.xml",
        "views/res_partner_views.xml",
        "views/stock_picking_views.xml"
    ],
}
