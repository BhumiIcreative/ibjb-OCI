# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields,api
from odoo.addons.ibjb_studio import common


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    badge = fields.Char(_('BadgeID'),related='employee_id.barcode')

    @api.model
    def update_hr_attendance_studio_fields(self):
        print('\n\n\nmethod called')

        migration_fields = {
            "x_studio_field_tYFkc": "badge",
        }

        attendances = self.search([])
        print('\n\n\nhr_attendances', attendances)  # Fetch all attendance records
        for rec in attendances:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
