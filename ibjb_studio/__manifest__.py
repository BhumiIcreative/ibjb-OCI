# coding: utf-8
{
    "name": "IBJB Studio",
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
    ],
    "data": [
        "data/action_add_fields.xml",
        "report/report_purchase.xml",
        "report/ir_actions_report_templates.xml",
        "views/sale_subscription_views.xml",
        "views/partner_view.xml",
        "views/purchase_views.xml",
        "views/sale_order_views.xml",
    ],
}
