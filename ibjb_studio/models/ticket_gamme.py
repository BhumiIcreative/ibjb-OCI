# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class TicketGamme(models.Model):
    _name = 'ticket.gamme'
    _description = 'Ticket Gamme'

    name = fields.Char()
