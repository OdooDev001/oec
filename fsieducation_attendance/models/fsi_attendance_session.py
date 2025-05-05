# -*- coding: utf-8 -*-
###############################################################################
#
#    FSI Inc
#    Copyright (C) 2005-TODAY FSI Inc(<https://fsibgroup.com/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import models, fields


class FSISession(models.Model):
    _inherit = "fsi.session"

    attendance_sheet = fields.One2many('fsi.attendance.sheet',
                                       'session_id', string='Session')

    def get_attendance(self, context=None):
        """To get attendance details"""
        sheet = self.env['fsi.attendance.sheet'].search(
            [('session_id', '=', self.id)])
        register = self.env['fsi.attendance.register'].search(
            [('course_id', '=', self.course_id.id),
             ('batch_id', '=', self.batch_id.id)])
        if self.id == sheet.session_id.id:
            if len(sheet) <= 1:
                view_id = self.env.ref('fsieducation_attendance.'
                                       'view_fsi_attendance_sheet_form').id,
                return {
                    'name': 'Attendance Sheet',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'views': [(view_id, 'form')],
                    'res_model': 'fsi.attendance.sheet',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'target': 'current',
                    'res_id': sheet.id,
                    'context': {'default_session_id': self.id,
                                'default_register_id': [rec.id for rec in register]},
                    'domain': [('session_id', "=", sheet.session_id.id)]
                }
            action = self.env.ref('fsieducation_attendance.'
                                  'action_open_fsi_attendance_sheet_view').read()[0]
            action['domain'] = [('session_id', '=', self.id)]
            action['context'] = {
                'default_session_id': self.id,
                'default_register_id': [rec.id for rec in register]}
            return action
        else:
            view_id = self.env.ref('fsieducation_attendance.'
                                   'view_fsi_attendance_sheet_form').id,
            return {
                'name': 'Attendance Sheet',
                'view_type': 'form',
                'view_mode': 'list',
                'views': [(view_id, 'form')],
                'res_model': 'fsi.attendance.sheet',
                'view_id': False,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'context': {'default_session_id': self.id,
                            'default_register_id': [rec.id for rec in register]},
                'domain': [('session_id', "=", self.id)]
            }
