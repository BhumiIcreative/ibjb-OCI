# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    vat_customer = fields.Char(
        related="partner_id.vat",
        readonly=True,
        store=True,
        string="Customer VAT No.",
        help="Tax identification number. Complete this if the contact is subject to government "
             "taxes. Used in some legal statements")
    oci_codetiersfact = fields.Char(
        string="Third party code",
        related="partner_id.customer_code",
        readonly=True,
        Store=True
    )
    oci_compta_langcustomer = fields.Selection(
        [],
        related="partner_id.field_aD1p5",
        readonly=True,
        help="All emails and documents sent to this contact will be translated into this language.",
        string="Customer language"
    )
    amount_tax_signed_stored = fields.Monetary(
        compute="_compute_amount_tax_signed_stored",
        string="VAT",
        store=True,
    )

    @api.depends("amount_tax_signed", "invoice_line_ids")
    def _compute_amount_tax_signed_stored(self):
        """
            This method computes the value of 'amount_tax_signed_stored' field
            based on the 'amount_tax_signed' field. It is dependent on the
            'amount_tax_signed' and 'invoice_line_ids' fields, ensuring that
            the stored value is recalculated when these fields are updated.
        """
        for record in self:
            record.amount_tax_signed_stored = record.amount_tax_signed
