# coding: utf-8
{
    "name": "BOY helpdesk ticket",
    "summary": "BOY helpdesk ticket",
    "description": """
        Allow user to link Helpdesk ticket with crm and maintenance""",
    "author": "Aktiv software",
    "license":"LGPL-3",
    "website": "http://www.aktivsoftware.com",
    "category": "Helpdesk",
    "version": "17.0.1.0.0",
    "depends": [
        "helpdesk",
        "crm",
        "sale_crm",
        "oci_sav",
        "hr_maintenance",
    ],
    "data": [
        "views/helpdesk_ticket_views.xml",
        "views/maintenance_request_form_view.xml",
        "views/crm_lead_form_view.xml",
    ],
}
