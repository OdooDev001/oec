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
from odoo.tests import common


class TestAttendanceCommon(common.TransactionCase):
    def setUp(self):
        super(TestAttendanceCommon, self).setUp()
        self.fsi_attendance_register = self.env['fsi.attendance.register']
        self.fsi_attendance_sheet = self.env['fsi.attendance.sheet']
        self.fsi_attendance_line = self.env['fsi.attendance.line']
        self.fsi_attendance_wizard = self.env['student.attendance']
