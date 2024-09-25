# -*- coding: utf-8 -*-
from odoo import fields, models, _
from odoo.addons.ibjb_studio import common


class ProductTemplate(models.Model):
    _inherit = "product.template"

    article_codedouane = fields.Char(
        string=(_("Customs code")),
        copy=False,
        store=True,
    )
