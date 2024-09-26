# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields,_


class TicketGamme(models.Model):
    _name = 'ticket.gamme'

    name = fields.Char()
