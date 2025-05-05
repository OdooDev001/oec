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

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class FSIProgram(models.Model):
    _name = "fsi.program"
    _inherit = "mail.thread"
    _description = "FSI Program"

    name = fields.Char('Name', required=True, translate=True, tracking=True)
    code = fields.Char('Code', size=16, required=True, translate=True)
    max_unit_load = fields.Float("Maximum Unit Load")
    min_unit_load = fields.Float("Minimum Unit Load")
    department_id = fields.Many2one(
        'fsi.department', 'Department',
        default=lambda self:
        self.env.user.dept_id and self.env.user.dept_id.id or False)
    active = fields.Boolean(default=True)
    image_1920 = fields.Image('Image', attachment=True)
    program_level_id = fields.Many2one(
        'fsi.program.level', 'Program Level',required=True)


class OpProgramLevel(models.Model):
    _name = "fsi.program.level"
    _inherit = "mail.thread"
    _description = "FSI Program level"

    name = fields.Char('Name', required=True, translate=True, tracking=True)
