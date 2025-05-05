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
from odoo import models, fields, api


class FSIAttendanceRegister(models.Model):
    _name = "fsi.attendance.register"
    _inherit = ["mail.thread"]
    _description = "Attendance Register"
    _order = "id DESC"

    name = fields.Char(
        'Name', size=16, required=True, tracking=True)
    code = fields.Char(
        'Code', size=16, required=True, tracking=True)
    course_id = fields.Many2one(
        'fsi.course', 'Course', required=True, tracking=True)
    batch_id = fields.Many2one(
        'fsi.batch', 'Batch', required=True, tracking=True)
    subject_id = fields.Many2one(
        'fsi.subject', 'Subject', tracking=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_attendance_register_code',
         'unique(code)', 'Code should be unique per attendance register!')]

    @api.depends('course_id')
    def onchange_course(self):
        """To change the batch_id field based on course"""
        if not self.course_id:
            self.batch_id = False
