# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.addons.ibjb_studio import common


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
