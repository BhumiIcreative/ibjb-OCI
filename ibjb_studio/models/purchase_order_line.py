# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    oci_product_reference = fields.Char(
        related="product_id.property_account_expense_id.display_name",
        string="Product Reference",
        readonly=True,
        copy=False,
    )  # No need to migarte this fields as it is related field
