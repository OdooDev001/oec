# -*- coding: utf-8 -*-
###############################################################################
#
#    FSI Inc
#    Copyright (C) 2009-TODAY FSI Inc(<https://fsibgroup.com/>).
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


class FSIClassroom(models.Model):
    _name = "fsi.classroom"
    _description = "Classroom"

    name = fields.Char('Name', size=16, required=True)
    code = fields.Char('Code', size=16, required=True)
    course_id = fields.Many2one('fsi.course', 'Course')
    batch_id = fields.Many2one('fsi.batch', 'Batch')
    capacity = fields.Integer(string='No of Person')
    facilities = fields.One2many('fsi.facility.line', 'classroom_id',
                                 string='Facility Lines')
    asset_line = fields.One2many('fsi.asset', 'asset_id',
                                 string='Asset')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_classroom_code',
         'unique(code)', 'Code should be unique per classroom!')]

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False
