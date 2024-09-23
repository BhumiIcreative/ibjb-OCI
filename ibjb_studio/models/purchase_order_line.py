# -*- coding: utf-8 -*-
from odoo import fields, models, _


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    oci_product_reference = fields.Char(
        related="product_id.property_account_expense_id.display_name",
        string=(_("Product Reference")),
        readonly=True,
        copy=False,
    )
