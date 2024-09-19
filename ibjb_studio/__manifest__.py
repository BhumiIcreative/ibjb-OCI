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
    'depends': ['base', 'contacts','helpdesk', 'l10n_fr','project','stock','crm','maintenance'],
    # always loaded
    'data': [
        "views/res_company_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_source_views.xml"
    ],
}
