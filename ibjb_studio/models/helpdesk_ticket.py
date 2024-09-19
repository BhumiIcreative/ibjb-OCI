# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields


class ResCompany(models.Model):
    _inherit = 'helpdesk.ticket'

    alerte_sq = fields.Boolean(_('Alert SQ'))  # x_studio_alerte_sq
    oci_asst_ouinonfp = fields.Boolean(_('Progress Sheet'))  # x_studio_oci_asst_ouinonfp
    ouverture_fiche_progres = fields.Selection([('Oui', 'Yes'), ('Non', 'No')],
                                               _('Opening Progress Sheet'))  # x_studio_ouverture_fiche_progres
    precisions = fields.Char(_('Details'))  # x_studio_precisions
    tache_ficheprogres_id = fields.Many2one('project.task', _('Progress sheet:')) # x_studio_tache_ficheprogres:
    assistance_article_id = fields.Many2one('product.product',_('Product reference'))  # x_studio_assistance_article
    assistance_numerolot_id = fields.Many2one('stock.lot',_('Batch/Serial number')) # x_studio_assistance_numerolot
    ouvert_le = fields.Datetime(_('Open on')) # x_studio_ouvert_le
    ouvert_par_id = fields.Many2one('res.users',_('Opened by'))  # x_studio_ouvert_par
    assistance_maintenance_ids = fields.Many2many('maintenance.request',string=_('Existing maintenance'))
    field_AxWS3 = fields.Many2many('crm.lead',string=_('Existing opportunity'))