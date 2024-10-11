# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields
from odoo.addons.ibjb_studio import common


class ResCompany(models.Model):
    _inherit = 'res.company'

    fax_soc = fields.Char(_('Fax'), store=True)      # x_studio_fax_soc
    oci_rcs = fields.Char(_('RCS'), store=True)      # x_studio_oci_rcs
    version = fields.Char(_('Version'), store=True)  # x_studio_version

    def update_company_studio_fields(self):
        print('\n\n\nmethod called')

        migration_fields = {
            "x_studio_fax_soc": "fax_soc",
            "x_studio_oci_rcs": "oci_rcs",
            "x_studio_version": "version",
        }

        company_orders = self.search([])
        print('\n\n\nmainten_orders', company_orders)  # Fetch all sale  records
        for rec in company_orders:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)

