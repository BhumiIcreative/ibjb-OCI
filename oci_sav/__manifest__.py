# -*- coding: utf-8 -*-

{
    "name": "OCI SAV",
    "summary": "OCI SAV",
    "description": "The module has Buttons create opportunity and create maintenance added from ticket",
    "version": "17.0.1.0.0",
    "author": "Aktiv software",
    "website": "http://www.aktivsoftware.com",
    "license": "AGPL-3",
    "category": "Helpdesk",
    "depends": ["helpdesk", "maintenance", "crm"],
    "data": [
        "views/crm_lead_views.xml",
        "views/maintenance_request_views.xml",
        "views/helpdesk_ticket_views.xml",
    ],
    "pre_init_hook": "pre_init_hook",
}
