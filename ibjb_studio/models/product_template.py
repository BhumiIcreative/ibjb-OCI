# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    article_codedouane = fields.Char(
        string="Customs code",
        copy=False,
        store=True,
    )
    oci_famille_article_id = fields.Many2one(
        'family',
        string="Famille d'article",
        copy=False,
    )
    is_delete = fields.Boolean(string="delete", copy=False)
    qty_av = fields.Boolean(string="qty_av",
                            copy=False)
    immuno_hemato_id = fields.Many2one('immuno.hemato', string='IMMUNO-HEMATO')
    gamme_article_ids = fields.Many2many('ticket.gamme', 'product_template_x_oci_ticket_gamme_rel', string='Gamme')
    product_tmpl_id_product_pricelist_item_count = fields.Integer("Product Template count", copy=False,
                                                                  compute='_compute_product_template_count')

    '''records for each product template and updates the count field.'''

    def _compute_product_template_count(self):
        for rec in self:
            rec.product_tmpl_id_product_pricelist_item_count = 0
            grouped_results = self.env['product.pricelist.item'].read_group(
                [('product_tmpl_id', 'in', self.ids)],
                ['product_tmpl_id'],
                ['product_tmpl_id'])
            product_template_counts = {result['product_tmpl_id'][0]: result['product_tmpl_id_count'] for result in
                                       grouped_results}
            rec.product_tmpl_id_product_pricelist_item_count = product_template_counts.get(rec.id, 0)
