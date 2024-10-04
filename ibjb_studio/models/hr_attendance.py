# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    badge = fields.Char(_('BadgeID'),related='employee_id.barcode')
