# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields,api
from odoo.addons.ibjb_studio import common


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    alerte_sq = fields.Boolean(_('Alert SQ'))  # x_studio_alerte_sq
    oci_asst_ouinonfp = fields.Boolean(_('Progress Sheet'))  # x_studio_oci_asst_ouinonfp
    ouverture_fiche_progres = fields.Selection([('Oui', 'Yes'), ('Non', 'No')],
                                               _('Opening Progress Sheet'))  # x_studio_ouverture_fiche_progres
    precisions = fields.Char(_('Details'))  # x_studio_precisions
    tache_ficheprogres_id = fields.Many2one('project.task', _('Progress sheet:'))  # x_studio_tache_ficheprogres:
    assistance_article_id = fields.Many2one('product.product', _('Product reference'))  # x_studio_assistance_article
    assistance_numerolot_id = fields.Many2one('stock.lot', _('Batch/Serial number'))  # x_studio_assistance_numerolot
    ouvert_le = fields.Datetime(_('Open on'))  # x_studio_ouvert_le
    ouvert_par_id = fields.Many2one('res.users', _('Opened by'))  # x_studio_ouvert_par
    assistance_maintenance_ids = fields.Many2many('maintenance.request', string=_('Existing maintenance'))  # x_studio_assistance_maintenance
    field_AxWS3 = fields.Many2many('crm.lead', string=_('Existing opportunity'))   # x_studio_field_AxWS3
    source_id = fields.Many2one('helpdesk.source', _('Source'))   # x_studio_source
    gamme_id = fields.Many2one('ticket.gamme', _('Range'))  # x_studio_gamme

    @api.model
    def update_helpdesk_ticket_studio_fields(self):
        print('\n\n\nmethod called')

        migration_fields = {
            "x_studio_alerte_sq": "alerte_sq",
            "x_studio_oci_asst_ouinonfp": "oci_asst_ouinonfp",
            "x_studio_ouverture_fiche_progres": "ouverture_fiche_progres",
            "x_studio_precisions": "precisions",
            "x_studio_tache_ficheprogres": "tache_ficheprogres_id",
            "x_studio_assistance_article": "assistance_article_id",
            "x_studio_assistance_numerolot": "assistance_numerolot_id",
            "x_studio_ouvert_le": "ouvert_le",
            "x_studio_ouvert_par": "ouvert_par_id",
            "x_studio_gamme": "gamme_id",
            "x_studio_source": "source_id",
            "x_studio_assistance_maintenance": "assistance_maintenance_ids",
            "x_studio_field_AxWS3": "field_AxWS3",
        }

        tickets = self.search([])
        print('\n\n\nhelpdesk_tickets', tickets)  # Fetch all helpdesk tickets
        for rec in tickets:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
