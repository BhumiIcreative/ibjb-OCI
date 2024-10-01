# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields


class HelpdeskSource(models.Model):
    _name = 'helpdesk.source'
    _description = 'Helpdesk Source'

    name = fields.Char()
