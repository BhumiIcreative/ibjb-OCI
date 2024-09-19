# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,_


class HelpdeskSource(models.Model):
    _name = 'helpdesk.source'

    name = fields.Char()
