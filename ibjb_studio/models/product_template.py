# -*- coding: utf-8 -*-
from odoo import fields, models, api


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
        translate=False,
    )
    is_delete = fields.Boolean(string="delete", copy=False, translate=False)
    qty_av = fields.Boolean(string="qty_av",
                            copy=False, translate=False)
    immuno_hemato_id = fields.Many2one('immuno.hemato', string='IMMUNO-HEMATO')
    gamme_article_ids = fields.Many2many('ticket.gamme', 'product_template_x_oci_ticket_gamme_rel', string='Gamme')
    product_tmpl_id_product_pricelist_item_count = fields.Integer("Product Template count", copy=False)
    #                                                               compute='_compute_product_template_count')
    #
    # def _compute_product_template_count(self):
    #     print("\n\n\nCOmpute---------------------")
    #     results = self.env['product.pricelist.item'].read_group(
    #         [('product_tmpl_id', 'in', self.ids)],
    #         ['product_tmpl_id'],
    #         ['product_tmpl_id']
    #     )
    #     print("\n\n\nresult:::::::::::::::", results)
    #     dict = {}
    #     for x in results: dict[x['product_tmpl_id'][0]] = x['product_tmpl_id_count']
    #     for record in self: record['product_tmpl_id_product_pricelist_item_count'] = dict.get(record.id, 0)
