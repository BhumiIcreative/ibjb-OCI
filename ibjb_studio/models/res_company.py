# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    fax_soc = fields.Char(_('Fax'), store=True)      # x_studio_fax_soc
    oci_rcs = fields.Char(_('RCS'), store=True)      # x_studio_oci_rcs
    version = fields.Char(_('Version'), store=True)  # x_studio_version
